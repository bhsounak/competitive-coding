array=[]
def getMaxSum(l, row, column):
	if row>=len(l):
		return 0
	if row==len(l)-1:
		return l[row][column]
	else:
		if array[row+1][column]==-1:
			array[row+1][column]=getMaxSum(l, row+1, column)
		if array[row+1][column+1]==-1:
			array[row+1][column+1]=getMaxSum(l, row+1, column+1)
		return max(l[row][column]+array[row+1][column], l[row][column]+array[row+1][column+1])

for _ in range(int(raw_input())):
	A=[]
	array=[]
	for _ in range(int(raw_input())):
		A.append(map(int, raw_input().split()))
		array.append([-1]*len(A[-1]))
	print getMaxSum(A, 0, 0)