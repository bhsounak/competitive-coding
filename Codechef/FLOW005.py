for _ in range(int(raw_input())):
	N=int(raw_input())
	count=0
	for i in [100, 50, 10, 5,2,1]:
		count=count+N/i
		N=N%i
	print count