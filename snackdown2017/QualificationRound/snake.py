for t in xrange(int(raw_input())):
	l = int(raw_input())
	s = raw_input()
	'''count_H=li.count('H')
	count_T=li.count('T')
	
	if count_T!=count_H:
		print 'Invalid
	
	if ''.join(sorted(li)) == s:
		print 'Valid'''
	flag,c=0,1
	for i in xrange(len(s)):
		if s[i]=='.':
			continue
		if s[i]=='H' and flag==0:
			flag=1
		elif s[i]=='T' and flag==1:
			flag=0

		else:
			c=0
			break
	if c==1 and flag==0:
		print "Valid"
	else:
		print 'Invalid'