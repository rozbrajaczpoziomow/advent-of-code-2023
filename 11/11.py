from math import *
from sys import *
from pprint import pprint as Print
path.append('..')
from aoccommons import *
from string import *
from itertools import *

def PART1(case):
	def ex(ls):
		ret = []
		for l in ls:
			if '#' not in l:
				ret += [l]
			ret += [l]
		return ret
	s = 0
	lines = []
	for line in case.readlines():
		lines += [line.strip()]
	lines = transpose(ex(transpose(ex(lines))))
	gala = []
	for (ri, r) in enumerate(lines):
		for (ci, c) in enumerate(r):
			if c == '#':
				gala += [(ri, ci)]
	# Print(gala)
	for ga, gb in combinations(gala, 2):
		s += abs(ga[0] - gb[0]) + abs(ga[1] - gb[1])

	return s


def PART2(case):
	s = 0
	lines = []
	for line in case.readlines():
		lines += [line.strip()]
	gala = []
	er = [ri for (ri, r) in enumerate(lines) if '#' not in r]
	ec = [ci for (ci, c) in enumerate(transpose(lines)) if '#' not in c]
	print(er,ec,sep='\n')
	for (ri, r) in enumerate(lines):
		for (ci, c) in enumerate(r):
			if c == '#':
				gala += [(ri, ci)]
	# Print(gala)
	for ga, gb in combinations(gala, 2):
		s += abs(ga[0] - gb[0]) + abs(ga[1] - gb[1])
		for ri in range(ga[0], gb[0], -1 if ga[0] > gb[0] else 1):
			if ri in er:
				s += 999999 * (ri in er)
		for ci in range(ga[1], gb[1], -1 if ga[1] > gb[1] else 1):
			if ci in ec:
				s += 999999 * (ci in ec)

	return s








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

	print()

if runPart2:
	print('Part 2:')

	if runTest:
		with open('test.txt', 'r') as f:
			print(f'- Test: {PART2(f)}')

	if runReal:
		with open('input.txt', 'r') as f:
			print(f'- Real: {PART2(f)}')