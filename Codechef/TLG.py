scores=[]
for _ in range(int(raw_input())):
	scores.append((map(int, raw_input().split())))

maxLead=lead=scores[0][0]-scores[0][1]
for i in range(1, len(scores)):
	lead=scores[i][0]-scores[i][1]+lead
	if abs(maxLead)<abs(lead):
		maxLead=lead
if maxLead<0:
	print '2 '+str(-maxLead)
else:
	print '1 '+str(maxLead)