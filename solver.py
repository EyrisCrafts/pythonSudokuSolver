import itertools

board = []

def load_board():
	f = open("puzzle.txt","r")	#The sudoku problem should be in 'puzzle.txt'
	for line in f:
		board.append(list(map(int,list(line.strip()))))
	f.close()
	return board

def printBoard():
	for line in board:
		print (' '.join(map(str,line)))

def row(hLine):
	return [i for i in board[hLine]]
		
def column(vLine):
	return [line[vLine] for line in board]

# Calculate and return the 3x3 box
def box(n):
	return [line[int((n%3)*3):int((n%3)*3+3)] for line in board[int((n//3)*3) : int(((n//3)*3)+3)]]

def isSolved():
	return not (0 in itertools.chain.from_iterable(board))

def solvehLine(hl,number):
	if number in row(hl):
		return
	marker = row(hl)
	for i in range(9):
		if marker[i] != 0:
			continue
		if number in column(i):
			continue
		b = list(itertools.chain.from_iterable(box((i//3) + (hl//3)*3)))
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
		b = list(itertools.chain.from_iterable(box((i//3) * 3  + vl//3)))
		if number in b:
			continue
		marker[i] = -1
	if marker.count(-1) != 1:
		return
	index=marker.index(-1)
	board[index][vl] = number

def solveBox(n,number):
	if number in list(itertools.chain.from_iterable(box(n))):
		return
	marker = box(n)
	for i in range(3):
		for j in range(3):
			if marker[i][j] != 0:
				continue
			if number in row(int(n//3)*3+i):
				continue
			if number in column(int(n%3)*3+j):
				continue
			
			board[int(n//3)*3+i][j+int(n%3)*3] = -1
	if ((list(itertools.chain.from_iterable(board))).count(-1) != 1):
		cleanBoard()
	else:
		index = findNumber(-1)
		if (index != (-1,-1)):
			board[index[0]][index[1]] = number

def findNumber(number):
	for i,line in enumerate(board):
		for j,boardNumber in enumerate(line):
			if boardNumber == number:
				return (i, j)
	return (-1,-1)
	

def cleanBoard():
	for i in range(9):
		for j in range(9):
			if (board[i][j] == -1):
				board[i][j] = 0

board = load_board()
print("Board loaded\n")
printBoard()
print ("\n\n")

iteration = 0

while(not isSolved()):
	iteration = iteration + 1
	print("Doing Iteraction "+str(iteration) + " \n")
	# Copy the board before attempting solve
	copyOfBoard = [x[:] for x in board]

	for i in range(9):
		for number in range(1,10):
			solvehLine(i,number)
			solvevLine(i,number)
			solveBox(i,number)
	
	# Check if there is any difference
	if (list(itertools.chain.from_iterable(copyOfBoard)) == list(itertools.chain.from_iterable(board))):
		break

if (isSolved()):
	print("Solved !\n")
	printBoard()
else:
	print("Stuck at Board\n")
	printBoard()

