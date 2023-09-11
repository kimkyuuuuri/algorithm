n= int(input())
e=int(input())
temp=0
for i in range(e):
    a,b = map(int, input().split())
    temp+=a*b

if temp==n:
    print('Yes')
else:
    print('No')
