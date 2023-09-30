
import sys
input=sys.stdin.readline
n=int(input())

answer=0
temp=list(map(int, input().split()))

if n==1:
    print(min(temp[0], temp[1]))
    exit(0)
    


for i in range(n-1):
    now = list(map(int, input().split()))
    
    # a1에서 a2
    a= temp[0]+now[0]
    # b1에서 a2
    b= temp[1]+temp[3]+now[0]

    # a1에서 b2
    c= temp[0]+temp[2]+now[1]
    # b1에서 b2
    d= temp[1]+now[1]

    
    answer1=min(a,b)
    answer2=min(c,d)
    
    if len(now)==2:
        break
    now[0]=answer1
    now[1]=answer2
    temp=now

print(min(answer1,answer2))


