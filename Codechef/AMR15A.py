for _ in range(int(raw_input())):
	A=map(int, raw_input().split())
	if len([e for e in A if e%2==0])>len(A)/2:
		print 'READY'
	else:
		print 'NOT READY'
