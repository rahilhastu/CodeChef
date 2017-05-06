for t in xrange(int(raw_input())):

	s = str(raw_input())
	flag =1
	start = s[0]

	for i in xrange(1,len(s)):
		next_char = s[i]

		if start == 'C':
			start=next_char
			continue

		elif start == 'E':
			if next_char=='C':
				flag=0
				break

		elif start=='S':
			if next_char!='S':
				flag=0
				break

		start = next_char

	if flag==1:
		print 'yes'

	else:
		print 'no'