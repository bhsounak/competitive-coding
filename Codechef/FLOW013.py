for _ in range(int(raw_input())):
	A=map(int, raw_input().split())
	if 0 in A or sum(A)!=180:
		print 'NO'
	else:
		print 'YES'