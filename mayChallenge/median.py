for t in range(int(raw_input())):

	n  = int(raw_input())
	a = [int(x) for x in raw_input().split()]
	a.sort()
	temp = a[n:]
	print temp[n/2]
	for i in range(n):
		print a[i],a[i+n],
	print
