from fractions import gcd

for _ in range(int(raw_input())):
	A, B=map(int, raw_input().split())
	print gcd(A,B), A*B/gcd(A,B)