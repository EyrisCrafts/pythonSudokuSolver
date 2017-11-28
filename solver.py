import itertools
## Empty Board will be updated
board = []

def load_board():
	f = open("puzzle.txt","r")	#The sudoku problem should be in 'puzzle.txt'
	for line in f:
		board.append(map(int,list(line.strip())))
	f.close()
	return board

def printBoard():
	for line in board:
		print ' '.join(map(str,line))

def row(hLine):
	return [i for i in board[hLine]]
		
def column(vLine):
	return [line[vLine] for line in board]

def box(n):
	return [line[(n%3)*3:(n%3)*3+3] for line in board[(n/3)*3:(n/3)*3+3]]

#working on Solving the box
def solveBox(n,number):
	if number in list(itertools.chain.from_iterable(box(n))):
		return
	marker =  list(itertools.chain.from_iterable(box(n)))
	
	
	for i in range(3):
		for j in range(3):
			if board[(n/3)*3+i][j+(n%3)*3] != 0:
				continue
			for l in  box(n):
				if number in l:
					continue
			if number in row((n/3)*3+i):
				continue
			if number in column((n%3)*3+j):
				continue
			board[(n/3)*3+i][j+(n%3)*3] = number

def solvehLine(hl,number):
	if number in row(hl):
		return
	marker = row(hl)
	for i in range(9):
		if marker[i] != 0:
			continue
		if number in column(i):
			continue
		b= list(itertools.chain.from_iterable(box((hl/3) * 3  + i%3 -1)))
		if number in b:
			continue
		marker[i] = -1
	if marker.count(-1) != 1:
		return
	index=marker.index(-1)
	board[hl][index] = number

def solvevLine(vl,number):
	if number in column(vl):
		return
	marker = column(vl)
	for i in range(9):
		if marker[i] != 0:
			continue
		if number in row(i):
			continue
		b= list(itertools.chain.from_iterable(box((i/3) * 3  + vl%3 -1)))
		if number in b:
			continue
		marker[i] = -1
	if marker.count(-1) != 1:
		return
	index=marker.index(-1)
	board[index][vl] = number



board = load_board()
printBoard()
print "\n\n"
solvevLine(4,6)
printBoard()

