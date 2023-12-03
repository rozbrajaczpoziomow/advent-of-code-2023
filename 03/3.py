from math import *
from sys import *
from pprint import pprint as Print
path.append('..')
from aoccommons import *
from string import *

def PART1(case):
	def sym(c):
		return c != '.' and not c.isnumeric()
	s = 0
	lines = []
	count = False
	num = ''
	for line in case.readlines(): lines += [line.strip()]
	for (li, line) in enumerate(lines):
		for (ci, char) in enumerate(line):
			if not char.isnumeric():
				if num == '':
					continue
				if count: s += int(num)
				num = ''
				count = False
				continue

			num += char
			if count:
				continue
			count |= ci != 0 and sym(line[ci - 1]) # <
			count |= ci != len(line) - 1 and sym(line[ci + 1]) # >
			count |= li != 0 and sym(lines[li - 1][ci]) # ^
			count |= li != len(lines) - 1 and sym(lines[li + 1][ci]) # v
			count |= li != 0 and ci != 0 and sym(lines[li - 1][ci - 1]) # ^<
			count |= li != 0 and ci != len(line) - 1 and sym(lines[li - 1][ci + 1]) # ^>
			count |= li != len(lines) - 1 and ci != 0 and sym(lines[li + 1][ci - 1]) # v<
			count |= li != len(lines) - 1 and ci != len(line) - 1 and sym(lines[li + 1][ci + 1]) # v>
	return s


def PART2(case):
	def sym(c):
		return c == '*'
	def inc(d, k):
		if k not in d:
			d[k] = 0
		d[k] += 1
	def scan(lines, li, ci):
		line = lines[li]
		real = ci
		while line[real].isnumeric():
			real -= 1
			if real == -1: break
		real += 1
		n = ''
		while line[real].isnumeric():
			n += line[real]
			real += 1
			if real == len(line):
				break
		print(len(line) - 1, real, n)
		return int(n)
	s = 0
	lines = []
	count = False
	num = ''
	used = {}
	for line in case.readlines(): lines += [line.strip()]
	for (li, line) in enumerate(lines):
		for (ci, char) in enumerate(line):
			if not char.isnumeric():
				num = ''
				count = False
				continue

			num += char
			if count:
				continue
			count |= ci != 0 and sym(line[ci - 1]) # <
			if count:
				inc(used, (li, ci-1))
				continue
			count |= ci != len(line) - 1 and sym(line[ci + 1]) # >
			if count:
				inc(used, (li, ci+1))
				continue
			count |= li != 0 and sym(lines[li - 1][ci]) # ^
			if count:
				inc(used, (li-1, ci))
				continue
			count |= li != len(lines) - 1 and sym(lines[li + 1][ci]) # v
			if count:
				inc(used, (li+1, ci))
				continue
			count |= li != 0 and ci != 0 and sym(lines[li - 1][ci - 1]) # ^<
			if count:
				inc(used, (li-1, ci-1))
				continue
			count |= li != 0 and ci != len(line) - 1 and sym(lines[li - 1][ci + 1]) # ^>
			if count:
				inc(used, (li-1, ci+1))
				continue
			count |= li != len(lines) - 1 and ci != 0 and sym(lines[li + 1][ci - 1]) # v<
			if count:
				inc(used, (li+1, ci-1))
				continue
			count |= li != len(lines) - 1 and ci != len(line) - 1 and sym(lines[li + 1][ci + 1]) # v>
			if count:
				inc(used, (li+1, ci+1))
				continue
	need = []
	for k in used.keys():
		if used[k] == 2: # only ever 1 or 2
			need += [k]

	for (li, ci) in need:
		line = lines[li]
		nums = []
		if ci != 0 and (line[ci - 1]).isnumeric(): # <
			nums += [scan(lines, li, ci-1)]
		if ci != len(line) - 1 and (line[ci + 1]).isnumeric(): # >
			nums += [scan(lines, li, ci+1)]
		if li != 0 and (lines[li - 1][ci]).isnumeric(): # ^
			nums += [scan(lines, li-1, ci)]
		if li != len(lines) - 1 and (lines[li + 1][ci]).isnumeric(): # v
			nums += [scan(lines, li+1, ci)]
		if li != 0 and ci != 0 and (lines[li - 1][ci - 1]).isnumeric(): # ^<
			nums += [scan(lines, li-1, ci-1)]
		if li != 0 and ci != len(line) - 1 and (lines[li - 1][ci + 1]).isnumeric(): # ^>
			nums += [scan(lines, li-1, ci+1)]
		if li != len(lines) - 1 and ci != 0 and (lines[li + 1][ci - 1]).isnumeric(): # v<
			nums += [scan(lines, li+1, ci-1)]
		if li != len(lines) - 1 and ci != len(line) - 1 and (lines[li + 1][ci + 1]).isnumeric(): # v>
			nums += [scan(lines, li+1, ci+1)]
		g = [*set(nums)]
		s += g[0] * g[1]
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

if runPart2:
	print('\nPart 2:')

	if runTest:
		with open('test.txt', 'r') as f:
			print(f'- Test: {PART2(f)}')

	if runReal:
		with open('input.txt', 'r') as f:
			print(f'- Real: {PART2(f)}')
