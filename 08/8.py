from math import *
from sys import *
from pprint import pprint as Print
path.append('..')
from aoccommons import *
from string import *

def PART1(case):
	s = 0
	paths = {}
	dr = []
	for line in case.readlines():
		if len(dr) == 0:
			dr = [*map(int, line.strip().replace('R','1').replace('L','0'))]
			continue
		if line.strip() == '':
			continue
		t,d=line.strip().split(' = ')
		d=d[1:-1].split(', ')
		paths[t]=(d[0],d[1])
	# Print(paths)
	idx = 0
	cur = 'AAA'
	while cur != 'ZZZ':
		cur = paths[cur][dr[idx]]
		idx += 1
		if idx == len(dr):
			idx = 0
		s += 1
	return s


def PART2(case):
	s = 0
	paths = {}
	dr = []
	st = []
	mark = []
	for line in case.readlines():
		if len(dr) == 0:
			dr = [*map(int, line.strip().replace('R','1').replace('L','0'))]
			continue
		if line.strip() == '':
			continue
		t,d=line.strip().split(' = ')
		d=d[1:-1].split(', ')
		paths[t]=(d[0],d[1])
		if t[2] == 'A':
			st += [t]
	# Print(paths)
	print(len(st))
	idx = 0
	end = []
	g = False
	for _ in range(len(st)): mark += [False]
	fn = [-1]*len(st)
	s = 0
	while len(st) != 0:
		for (ic, cur) in enumerate(st):
			cur = paths[cur][dr[idx]]
			print(s)
			Print(fn)
			print('--')
			if cur[2] == 'Z':
				if fn[ic] != -1:
					end += [(cur, s-fn[ic])]
					mark[ic] = True
					g = True
				else:
					fn[ic] = s
			st[ic] = cur
		s += 1
		idx += 1
		if idx == len(dr):
			idx = 0
		# print(s,st)
		if g:
			for (im, m) in enumerate(mark):
				if m:
					st.pop(im)
					mark[im] = False
					break
		if s > 10: break
	Print(end)
	# return sum(map(lambda x:x[1],end))


# run all individually
# measure how many cycles it takes for them to go from XXZ -> XXZ again
# save that in a list
# do it for all
# multiply every element in the list
# return

# TODO: fix ^





runPart1 = runPart2 = True
runReal = runTest = True

if '-1' in argv: runPart2 = False
if '-2' in argv: runPart1 = False
if '-t' in argv: runReal = False
if '-r' in argv: runTest = False

if runPart1:
	print('Part 1:')

	if runTest:
		with open('test~1.txt', 'r') as f:
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