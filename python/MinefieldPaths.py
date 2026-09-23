grid = [
    [0, 0, 1],
    [0, 0, 0],
    [1, 0, 0]
]

def printM(Matrix):
	for v in Matrix:
		for y in v:
			print(y,end="")
		print("")
	print("==============================")

def findpath(Matrix,r,c):
	if r >= len(Matrix) or c >= len(Matrix[0]) or r < 0 or c < 0 :
		return 0
	if Matrix[r][c] != 0:
		return 0
	if r == len(Matrix) - 1 and c == len(Matrix[0]) - 1:
		return 1
	num = 0
	Matrix[r][c] = "."
	printM(grid)
	num += findpath(Matrix,r + 0,c + 1)
	num += findpath(Matrix,r + 0,c - 1)
	num += findpath(Matrix,r + 1,c + 0)
	num += findpath(Matrix,r - 1,c + 0)
	Matrix[r][c] = 0
	return num

printM(grid)
print(findpath(grid,0,0))