# 큰 수의 법칙
n,m,k=map(int,input().split())
data=list(map(int,input().split()))

data.sort()
count=0
num=0
for i in range (m):
    if count== k:
        num+=data[n-2]
        count=0
    else: 
        num+=data[n-1]
        count+=1

print(num)
    
