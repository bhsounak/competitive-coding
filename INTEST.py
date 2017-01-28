n,k=map(int, raw_input().split())
count=0
for _ in range(n):
	if int(raw_input())%k==0:
		count+=1
print count