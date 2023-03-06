# 재귀로 구현
def fibo(n):
        if n==1:
                return 1
        elif n==2:
                return 1
        else:
                return fibo(n-2)+fibo(n-1)


n=int(input())
print(fibo(n))

# 반복으로 구현
# 배열에 기록
def fibo_2(n):
        d=[0]*(n+1)  
        d[1]=1
        d[2]=1
        for i in range(3,n+1):
                d[i]=d[i-1]+d[i-2]
        print(d[n])
        

b=int(input())
fibo_2(b)
