from math import *
from sys import *
from pprint import pprint as Print
path.append('..')
from aoccommons import *
from string import *

def PART1(case):
	s = 0
	for line in case.readlines():
		pass

def PART2(case):
	s = 0
	for line in case.readlines():
		pass








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