from math import log
for _ in range(int(raw_input())):
	N=int(raw_input())
	count=0
	for i in range(1, int(log(N, 5))+1):
		count+=N/(5**i)
	print count