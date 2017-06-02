def ans(s):
	for i in range(len(s)):
		if s[i]=='m':
			if (s[i-1]=='s' and i!=0):
				s[i-1]=0
			elif (s[i+1]=='s' and i!=(len(s)-1)):
				s[i+1]=0
			else:
				continue
		else:
			continue
	mc=0
	sc=0
	for i in range(len(s)):
		if s[i]=='s':
			sc+=1
		elif s[i]=='m':
			mc+=1
		else:
			continue
	if sc>mc:
		return 'snakes'
	elif mc>sc:
		return 'mongooses'
	else:
		return 'tie'

for t in range(int(raw_input())):
	s = str(raw_input())
	s=list(s)
	print ans(s),'\n'