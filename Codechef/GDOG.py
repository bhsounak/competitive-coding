for _ in range(int(raw_input())):
	N,K=map(int, raw_input().split())
	maxI=2
	maxCoins=N%2
	for i in range(3,K+1):
		if maxCoins<N%i:
			maxI=i
			maxCoins=N%i
	print maxCoins
