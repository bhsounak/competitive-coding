for _ in range(int(raw_input())):
	s=raw_input()
	print 'wins' if s==s[::-1] else 'losses'