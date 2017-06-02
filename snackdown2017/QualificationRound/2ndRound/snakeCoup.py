def fence(a,b,n):
	#bool hori = a.index('*')>=0 and b.index('*')>=0

	if a.index('*')>=0 and b.index('*')>=0:
		f=int(1)
	else:
		f=int(0)	

	prod = [False,False]
	for i in range(n):
		for k in range(0,2):
			if a[i]=='*' or b[i]=='*':
				if prod[k]:
					f+=1
					prod[0]==prod[1]==False
					break
		for k in range(0,2):
			if a[k]=='*' and b[k]=='*':
				prod[k]=True
	return f


for _ in range(int(raw_input())):

	n = int(raw_input())
	a = str(raw_input())
	b = str(raw_input())

	print fence(a,b,n)