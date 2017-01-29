for _ in range(int(raw_input())):
	L,R=map(int, raw_input().split())
	s=0
	for i in range(L, R+1):
		if str(i)==str(i)[::-1]:
			s=s+i
	print s