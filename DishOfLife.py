for t in range(int(raw_input())):
	n,k = map(int,raw_input().split())
	a = [x for x in range(1,k+1)]
	ans=[]
	flag=0
	sf=0
	#for e in range(n):
	'''p=[[int(i) for i in raw_input().split()]for q in range(n)]
	for y in range(0,len(p)):
		for g in range(1,p[y][0]+1):
			if p[y][g] not in ans:
				ans.append(p[y][g])
			if ans == a:
				flag=1
				break
		if flag == 1:
			break
#	print y,g,ans,a
	if flag==1:
		if (y+1==n):
			print 'all'
		else:
			print 'some'
	else:
		print 'sad''
	'''
	for i in range(0,n):
		c = int(raw_input())
		sf=0
		for s in range(0,c):
			f = int(raw_input())
			if f not in ans:
				sf+=1
				ans.append(f)
		if(sf==c and i!=n-1):
			flag=1

	if ans!=a:
		print 'sad'
	elif flag ==1:
		print 'some'
	else:
		print 'all'