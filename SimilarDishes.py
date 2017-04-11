for t in range(int(raw_input())):
	p = [str(x) for x in raw_input().split()]
	q = [str(y) for y in raw_input().split()]
	
	count=0
	for i in p:
		for j in q:
			if i==j:
				count+=1
			#if count ==2:
			#	break
	if count >=2:
		print "similar"
	else:
		print "dissimilar"
