n=int(input())

def fibo(x):
    global one
    global zero
    if(x==0):
        return 0
    if x==1 or x==2:
        return 1
 
    if d[x] != 0:
    	return d[x]
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

for i in range(n):
    d=[0]*42
    a=int(input())
    if(a==0):
        print(1,end=' ')
    else:
        print(fibo(a-1), end=' ')
    print(fibo(a))

