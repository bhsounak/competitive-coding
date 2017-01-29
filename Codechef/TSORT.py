A=[]
for _ in range(int(raw_input())):
	A.append(int(raw_input()))

print '\n'.join(map(str,sorted(A)))