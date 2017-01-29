while True:
	n=int(raw_input())
	if n==0:
		break
	A=map(int, raw_input().split())
	B=[0]*n
	for i in range(n):
		B[A[i]-1]=i+1
	if B==A:
		print 'ambiguous'
	else:
		print 'not ambiguous'

