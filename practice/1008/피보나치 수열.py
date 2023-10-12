n=int(input())
array=[0]*(n+1)
def fibo(x):
    if x==0 or x==1:
        return 1
    elif array[x]!=0:
        return array[x]
    else:
        array[x]=fibo(x-1)+fibo(x-2)
        return array[x]
print(fibo(n))
