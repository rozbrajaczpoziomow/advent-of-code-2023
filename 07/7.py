from math import *
from sys import *
from pprint import pprint as Print
path.append('..')
from aoccommons import *
from string import *

def PART1(case):
	kards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', "6", '5', '4', '3', '2']
	s = 0
	K = {'5': [], '4': [], 'fh': [], '2': [], '2p': [], '1p': [], 'hc': []}
	Bs = {}
	for line in case.readlines():
		c, bid = line.split(' ')
		bid = int(bid)
		Bs[c] = bid
		rank = 0
		g = {}
		for l in c:
			g[l] = c.count(l)
		# print([*sorted(g.values())])
		if [*sorted(g.values())] == [5]:
			K['5'] += [c]
		elif [*sorted(g.values())] == [1, 4]:
			K['4'] += [c]
		elif [*sorted(g.values())] == [2, 3]:
			K['fh'] += [c]
		elif [*sorted(g.values())] == [1, 1, 3]:
			K['2'] += [c]
		elif [*sorted(g.values())] == [1, 2, 2]:
			K['2p'] += [c]
		elif [*sorted(g.values())] == [1, 1, 1, 2]:
			K['1p'] += [c]
		elif [*sorted(g.values())] == [1, 1, 1, 1, 1]:
			K['hc'] += [c]
	rank = 1
	for k in [*K.keys()][::-1]:
		v = K[k]
		real = [*sorted(v, reverse=1, key=lambda x: [*map(kards.index, x)])]
		# print(k, real)
		for f in real:
			bid = Bs[f]
			s += rank * bid
			rank += 1
	return s


def PART2(case):
	kards = ['A', 'K', 'Q', 'T', '9', '8', '7', "6", '5', '4', '3', '2', 'J']
	def perm(c):
		if c == 'JJJJJ':
			return ['AAAAA']
		ret = []
		ls = [*set(c)]
		for l in ls:
			if l == 'J': continue
			ret += [c.replace('J', l)]
		return ret
	s = 0
	K = {'5': [], '4': [], 'fh': [], '2': [], '2p': [], '1p': [], 'hc': []}
	Bs = {}
	for line in case.readlines():
		C, bid = line.split(' ')
		bid = int(bid)
		Bs[C] = bid
		rank = 0
		if 'J' in C:
			options = perm(C)
		else:
			options = [C]
		key = ''
		# print(C, options)
		for c in options:
			gk = ''
			g = {}
			for l in c:
				g[l] = c.count(l)
			# print([*sorted(g.values())])
			if [*sorted(g.values())] == [5]:
				gk = '5'
			elif [*sorted(g.values())] == [1, 4]:
				gk = '4'
			elif [*sorted(g.values())] == [2, 3]:
				gk = 'fh'
			elif [*sorted(g.values())] == [1, 1, 3]:
				gk = '2'
			elif [*sorted(g.values())] == [1, 2, 2]:
				gk = '2p'
			elif [*sorted(g.values())] == [1, 1, 1, 2]:
				gk = '1p'
			elif [*sorted(g.values())] == [1, 1, 1, 1, 1]:
				gk = 'hc'
			# print(len(gk))
			if [*K.keys()].index(gk) < ([*K.keys()].index(key) if key != '' else i9e9):
				key = gk
		K[key] += [C]
		# print('------')
	rank = 1
	for k in [*K.keys()][::-1]:
		v = K[k]
		real = [*sorted(v, reverse=1, key=lambda x: [*map(kards.index, x)])]
		# print(k, real)
		for f in real:
			bid = Bs[f]
			s += rank * bid
			rank += 1
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