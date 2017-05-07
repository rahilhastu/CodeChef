from operator import mul
def se(a):
    return reduce(lambda res, j: res + [subset + [j] for subset in res],a, [[]])

n,k = map(int,raw_input().split())
a = map(int,raw_input().split())

counter = 0
powerset = se(a)
#print s
for i in powerset:
    x = i[:]
    #print x
    if len(x)>0:
        ans = reduce(mul,x)
 #       print ans
        if k<ans:  
            counter += 1
print (2**n-1)-counter