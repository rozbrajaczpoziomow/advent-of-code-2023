from math import *
from sys import *
from pprint import pprint as Print
path.append('..')
from aoccommons import *
from string import *

def PART1(case):
	s = 0
	games = {}
	for line in case.readlines():
		_id = line.split(' ')[1].split(':')[0]
		contents = []
		for c in line.strip().split(': ')[1].split('; '):
			a = [*map(lambda x:x[::-1],sorted([*map(lambda x:x[::-1], c.split(', '))]))]
			C = {}
			for g in a:
				C[g.split(' ')[1][0]] = int(g.split(' ')[0])
			C['r'] = C['r'] if C.get('r') != None else 0
			C['g'] = C['g'] if C.get('g') != None else 0
			C['b'] = C['b'] if C.get('b') != None else 0
			contents += [C]
		games[_id] = contents

	possible = []
	for gid in games.keys():
		cont = games[gid]
		for time in cont:
			if time['r'] > 12 or time['g'] > 13 or time['b'] > 14:
				break
		else:
			possible += gid,
	print(possible)
	return sum(map(int, possible))

def PART2(case):
	s = 0
	games = {}
	for line in case.readlines():
		_id = line.split(' ')[1].split(':')[0]
		contents = []
		for c in line.strip().split(': ')[1].split('; '):
			a = [*map(lambda x:x[::-1],sorted([*map(lambda x:x[::-1], c.split(', '))]))]
			C = {}
			for g in a:
				C[g.split(' ')[1][0]] = int(g.split(' ')[0])
			C['r'] = C['r'] if C.get('r') != None else 0
			C['g'] = C['g'] if C.get('g') != None else 0
			C['b'] = C['b'] if C.get('b') != None else 0
			contents += [C]
		games[_id] = contents

	possible = []
	for gid in games.keys():
		cont = games[gid]
		rm = gm = bm = 0
		for time in cont:
			rm = max(rm, time['r'])
			gm = max(gm, time['g'])
			bm = max(bm, time['b'])
		print(gid,rm,gm,bm)
		possible += [rm*gm*bm]
	print(possible)
	return sum(map(int, possible))








runPart1 = runPart2 = True
runReal = runTest = True

if '-1' in argv: runPart2 = False
if '-2' in argv: runPart1 = False
if '-t' in argv: runReal = False
if '-r' in argv: runTest = False

if runPart1:
	print('Part 1:')

	if runTest:
		with open('test.txt', 'r') as f:
			print(f'- Test: {PART1(f)}')

	if runReal:
		with open('input.txt', 'r') as f:
			print(f'- Real: {PART1(f)}')

if runPart2:
	print('\nPart 2:')

	if runTest:
		with open('test.txt', 'r') as f:
			print(f'- Test: {PART2(f)}')

	if runReal:
		with open('input.txt', 'r') as f:
			print(f'- Real: {PART2(f)}')
