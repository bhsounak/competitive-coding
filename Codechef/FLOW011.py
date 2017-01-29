for _ in range(int(raw_input())):
	sal=int(raw_input())
	if sal<1500:
		print 2*sal
	else:
		print '%.1f' %(1.98*sal+500)