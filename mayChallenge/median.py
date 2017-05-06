for t in range(int(raw_input())):

	n  = int(raw_input())
	a = [int(x) for x in raw_input().split()]
	b = []
	for i in range(1,len(a)-2,2):
		if a[i]<a[i+1]:
			a[i],a[i+1]=a[i+1],a[i]

	#print a
	for i in range(0,(len(a))/2):
		max_ = max(a[2*i],a[2*i+1])
		b.append(max_)
	print b[len(b)/2]
	for i in a:
		print i,
	print