for i in range(int(raw_input())):
	s = int(raw_input())
	a = [int (x) for x in raw_input().split()]
	flag =0
	diff=1
	if s%2==0 or a[0]!=1:
		print 'no'

	else:
		mid = s/2
		l_a = a[:mid]
		for i in range(len(l_a)-1):
			if abs(l_a[i]-l_a[i+1])!=1:
				diff=0
				break
		r_a = a[mid+1:]
		#print l_a , r_a
		#l_a = l_a.sort()
		r_a.sort()
		#print l_a , r_a
		if diff==1:
			for i in range(len(l_a)):
				if l_a[i] == r_a[i]:
					flag =1
				else:
					flag=0
					break 
		if flag==1:
			print 'yes'
		else:
			print 'no'