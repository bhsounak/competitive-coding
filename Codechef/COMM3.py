def dist(P1, P2):
	return ((P1[0]-P2[0])**2+(P1[1]-P2[1])**2)**0.5

for _ in range(int(raw_input())):
	R=int(raw_input())
	L1=map(int, raw_input().split())
	L2=map(int, raw_input().split())
	L3=map(int, raw_input().split())
	if dist(L1, L2)>R and dist(L1, L3)>R or dist(L1, L2)>R and dist(L2, L3)>R or dist(L3, L2)>R and dist(L1, L3)>R:
		print 'no'
	else:
		print 'yes'
