def ans(q,a,n):
	count=0
	for i in range(n):
		if a[i]>=q:
			count+=1
			continue
		else:
			for k in range(i,n):
				for z in range(1,n-k):
					if a[k]+z >=q:
						count+=z
						n=n-z
						break
	return count

for _ in range(int(raw_input())):

	n,q = map(int,raw_input().split())

	a = [int (x) for x in raw_input().split()]

	for que in range(q):
		s = int(raw_input())
		a.sort(reverse=True)
		print ans(s,a,n)