from math import *
from sys import *
from pprint import pprint as Print
path.append('..')
from aoccommons import *
from string import *

def PART1(case):
	s = 0
	for line in case.readlines():
		line = line.split(': ')[1]
		card, win = [*map(lambda x: [*map(int, [*filter(lambda g: g != '', x.replace('  ', ' ').split(' '))])], line.split(' | '))]
		r = 1
		for w in win:
			if w in card:
				r *= 2
		s += r//2
	return s

def PART2(case):
	s = 0
	cards = {}
	cardcount = {}
	for line in case.readlines():
		cid, card = line.split(': ')
		# print(card)
		cid = int(cid.split(' ')[-1])
		card, win = [*map(lambda x: [*map(int, [*filter(lambda g: g != '', x.replace('  ', ' ').split(' '))])], card.split(' | '))]
		cards[cid] = [card, win]
		cardcount[cid] = 1
	# Print(cards)
	# print(cardcount)
	for cid in cards.keys():
		count = cardcount[cid]
		card, win = cards[cid]
		matching = 0
		for w in win:
			matching += w in card
		for n in range(cid+1,cid+1+matching):
			if n not in cardcount:
				break
			cardcount[n] += count

	# print(cardcount)
	return sum(cardcount.values())








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