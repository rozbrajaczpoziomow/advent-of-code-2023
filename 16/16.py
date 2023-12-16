from math import *
from sys import *
from pprint import pprint as Print
path.append('..')
from aoccommons import *
from string import *

def go(lines, dr):
	ch = []
	for line in lines:
		ch += [[*line]]
	energi = {(dr[1], dr[0]): True}
	beams = [dr]
	for iter in range(700):
		# print(iter, len(beams))
		tmp = beams[:]
		beams = []
		for beam in tmp:
			x, y, dx, dy = beam
			if y < 0 or x < 0 or y > len(ch) - 1 or x > len(ch[0]) - 1:
				continue # yeet the beam
			energi[(y, x)] = True
			split = False
			if ch[y][x] == '.':
				pass
				# beams += [(x, y, dx, dy)]
			elif ch[y][x] == '/':
				if dx == 1: # >
					# beams += [(x, y, 0, -1)] #^
					dx = 0; dy = -1
				elif dx == -1:
					# beams += [(x, y, 0, 1)] #v
					dx = 0; dy = 1
				elif dy == 1:
					# beams += [(x, y, -1, 0)] #<
					dx = -1; dy = 0
				elif dy == -1:
					# beams += [(x, y, 1, 0)] #>
					dx = 1; dy = 0
			elif ch[y][x] == '\\':
				if dx == 1: # >
					# beams += [(x, y, 0, 1)] #v
					dx = 0; dy = 1
				elif dx == -1:
					# beams += [(x, y, 0, -1)] #^
					dx = 0; dy = -1
				elif dy == 1: # >
					# beams += [(x, y, 1, 0)] #>
					dx = 1; dy = 0
				elif dy == -1:
					# beams += [(x, y, -1, 0)] #<
					dx = -1; dy = 0
			elif ch[y][x] == '|':
				if dx == 1 or dx == -1:
					# beams += [(x, y, 0, 1)]
					# beams += [(x, y, 0, -1)]
					dx = 0; dy = 1
					split = True
				# else:
					# beams += [(x, y, dx, dy)]
			elif ch[y][x] == '-':
				if dy == 1 or dy == -1:
					# beams += [(x, y, 1, 0)]
					# beams += [(x, y, -1, 0)]
					dx = 1; dy = 0
					split = True
				# else:
					# beams += [(x, y, dx, dy)]
			beams += [(x+dx, y+dy, dx, dy)]
			if split:
				beams += [(x-dx, y-dy, -dx, -dy)]
	# test
	# for (ri, r) in enumerate(lines):
	# 	for (ci, c) in enumerate(r):
	# 		if (ri, ci) in energi:
	# 			print(end='#')
	# 		else:
	# 			print(end='.')
	# 	print()
	# Print(energi)
	print(len(energi.keys()))
	return len(energi.keys())

def PART1(lines):
	return go(lines, (0, 0, 1, 0))

# pyfast  - real    1m12.795s
# python3 - real    1m35.225s
def PART2(lines):
	return max([
		go(lines, (0, 0, 1, 0)), # 6978
		go(lines, (0, 0, 0, 1)), # 6975
		go(lines, (0, len(lines) - 1, 1, 0)), # 47
		go(lines, (0, len(lines) - 1, 0, -1)), # 15
		go(lines, (len(lines[0]) - 1, 0, -1, 0)), # 3
		go(lines, (len(lines[0]) - 1, 0, 0, 1)), # 7000
		go(lines, (len(lines[0]) - 1, len(lines) - 1, 0, -1)), # 76
		go(lines, (len(lines[0]) - 1, len(lines) - 1, -1, 0)) # 2
	]) # none of which are correct answers btw lmao, I have no idea what's wrong with my code, especially since it works for p1








runPart1 = runPart2 = True
runReal = runTest = True

if '-1' in argv: runPart2 = False
if '-2' in argv: runPart1 = False
if '-t' in argv: runReal = False
if '-r' in argv: runTest = False

def read(file):
	with open(file, 'r') as f:
		ret = f.read().split('\n')
		if ret[-1] == '':
			return ret[:-1]
		return ret

if runPart1:
	print('Part 1:')

	if runTest:
		print(f'- Test: {PART1(read("test.txt"))}')

	if runReal:
		print(f'- Real: {PART1(read("input.txt"))}')

if runPart2:
	if runPart1:
		print()

	print('Part 2:')

	if runTest:
		print(f'- Test: {PART2(read("test.txt"))}')

	if runReal:
		print(f'- Real: {PART2(read("input.txt"))}')