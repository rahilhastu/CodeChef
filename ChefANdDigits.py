#only one test case passed !
def fun(l):
	count=0
	#f = dict(Counter(l))
	#print f
	e=[0]*10
	for i in l:
		i=int(i)
		e[i]=e[i]+1
	return e
		

for t in range(int(raw_input())):
	l,r=map(int,raw_input().split())
	a=[int(x) for x in raw_input().split()]
	f=[]
	p = r-l+1
	for y in range(l,r+1):
		l = list(str(y))
		#print l
		f=fun(l)
		#print f
		for i in range(10):
			if a[i]==f[i]:
				p-=1
				break
	print p