for _ in range(int(raw_input())):
	A,B=map(int, raw_input().split())
	if A==B:
		print '='
	elif A>B:
		print '>'
	else:
		print '<'