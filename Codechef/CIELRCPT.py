for _ in range(int(raw_input())):
	p=int(raw_input())
	count=0
	for i in range(11, -1, -1):
		count+=p/(2**i)
		p%=(2**i)
	print count