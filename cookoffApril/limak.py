for t in range(int(raw_input())):
	a,b = map(int,raw_input().split())
	l,bo,flag = 0 ,0,0
	for i in range(1,a+b):
		l+=2*i-1
		#print l
		bo+=2*i
		
		#print bo
		if l>a:
			flag=1
			break
		elif bo>b:
			flag=2
			break
			#print "Limak"
	if flag==1:
		print 'Bob'
	elif flag==2:
		print "Limak"