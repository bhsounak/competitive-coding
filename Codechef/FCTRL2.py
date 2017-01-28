def fact(n):
	p=1
	for i in range(2, n+1):
		p=p*i
	return p
	
for _ in range(int(raw_input())):
	print fact(int(raw_input()))