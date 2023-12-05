from math import *
from sys import *
from pprint import pprint as Print
path.append('..')
from aoccommons import *
from string import *

def PART1(case):
	s = 0
	lines = []
	for line in case.readlines():
		lines += [line]

	seeds = [*map(int,lines[0].split(': ')[1].split(' '))]
	mp = {}
	for gay in (''.join(lines)).split('\n\n')[1:]:
		print(gay)
		header,*vals = gay.split('\n')
		sts = []
		sts += [*filter(lambda x:x!='',vals)]

		# print('VEY GYA')

		# print(sts)
		# destRangeStart srcRangeStart rangeLen
		mp.clear()
		for l in sts:
			destRangeStart, srcRangeStart, rangeLen = [*map(int, l.strip().split(' '))]
			mp[range(srcRangeStart, srcRangeStart+rangeLen+1)] = destRangeStart - srcRangeStart

		print(mp)

		amp = []
		for s in seeds:
			mapped = s
			for r in mp.keys():
				if s in r:
					mapped += mp[r]
					print('found match for', s, mp[r], 'in range',r)
					break
			print(s, '>', mapped)
			amp += [mapped]
		seeds = amp
		print('----------')
	return min(seeds)

def PART2(case):
	s = 0
	lines = []
	for line in case.readlines():
		lines += [line]

	sd = [*map(int,lines[0].split(': ')[1].split(' '))]
	seeds = []
	for (i, v) in enumerate(range(0, len(sd), 2)):
		seeds += [*range(sd[v], sd[v]+sd[v+1]+1)]
	print('done with seeds')

	mp = {}
	for gay in (''.join(lines)).split('\n\n')[1:]:
		# print(gay)
		header,*vals = gay.split('\n')
		sts = []
		sts += [*filter(lambda x:x!='',vals)]

		# print('VEY GYA')

		# print(sts)
		# destRangeStart srcRangeStart rangeLen
		mp.clear()
		for l in sts:
			destRangeStart, srcRangeStart, rangeLen = [*map(int, l.strip().split(' '))]
			mp[(srcRangeStart, srcRangeStart+rangeLen+1)] = destRangeStart - srcRangeStart

		# print(mp)

		amp = []
		for s in seeds:
			mapped = s
			for r in mp.keys():
				if s >= r[0] and s < r[1]:
					mapped += mp[r]
					# print('found match for', s, mp[r], 'in range',r)
					break
			# print(s, '>', mapped)
			amp += [mapped]
		print('done iter')
		seeds = amp
		# print('----------')
	return min(seeds)








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