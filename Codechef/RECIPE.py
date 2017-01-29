from fractions import gcd
for _ in range(int(raw_input())):
	A=map(int, raw_input().split())[1:]
	g=A[0]
	for e in A[1:]:
		g=gcd(g, e)
	for e in A:
		print e/g,
	print