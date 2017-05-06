for t in range(int(raw_input())):
	n = int(raw_input())
	max_ = 0
	a = [int(x) for x in raw_input().split()]
	for j in range(len(a)):
		if max_<a[j]:
			max_ = a[j]

	print n-max_