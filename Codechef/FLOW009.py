for _ in range(int(raw_input())):
	q,p=map(float, raw_input().split())
	if q<=1000:
		print p*q
	else:
		print q*p*0.9