from math import *
from sys import *
from pprint import pprint as Print
path.append('..')
from aoccommons import *
from string import *

def PART1(case):
	lines = []
	for line in case.readlines():
		lines += [line]

	times = [*map(int, [*filter(lambda x: x != '', lines[0].split(' '))][1:])]
	dists = [*map(int, [*filter(lambda x: x != '', lines[1].split(' '))][1:])]
	out = 1
	for i in range(len(times)):
		time = times[i]
		dist = dists[i]
		ways = sum([speed * (time - speed) > dist for speed in range(1, time)])
		# ways = 0
		# for speed in range(1,time):
			# ways += speed * (time - speed) > dist
		# print('----')
		# print('done iter', ways)
		out *= ways
	return out

# Python3 does it in about 1.8s
# Pyfast does it in 300ms lmao
def PART2(case):
	lines = []
	for line in case.readlines():
		lines += [line]

	time = int(lines[0].replace(' ', '').split(':')[1])
	dist = int(lines[1].replace(' ', '').split(':')[1])
	# perf: binary search for beginning and end of set, sub max with min.
	print(time,dist)
	ways = sum([speed * (time - speed) > dist for speed in range(1, time)])
	return ways








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