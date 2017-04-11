def score(c,s):
	flag=0
	for i in range(len(s)-1):
		if s[i]=='1' and s[i+1]=='0':
			c+=1
			s[i]='0'
			flag=1
			cx=i
		elif ((s[i]=='0' and s[i+1]=='1') or (s[i]=='0' and i==len(s)-2)):
			if flag ==1:
				s[i]='1'
				c = c+(i-cx)
				score(c,s)
	return c
 	
for t in range(int(raw_input())):
	count = 0
	s = str(raw_input())
	s=s+'k'
	x=list(s)
	c=0
	print score(c,x)
	
