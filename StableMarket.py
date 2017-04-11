def fun(k,b):
	#print b
	count,result = 1,0
	j=0
	while (j<=len(b)-2):
		if(b[j]==b[j+1]):
			count+=1
		else:
			if(count>=k):
				result+=1		
			count =1
		j+=1
	return result
for t in range(int(raw_input())):
	n,q = map(int,raw_input().split())
	N = [int (x) for x in raw_input().split()]
	for e in range(0,q):
		count = 1
		l,r,k = map(int,raw_input().split())
		
		b=[]

		for r in range(l-1,r):
			b.append(N[r])
		b.append(-1)
		print fun(k,b)
