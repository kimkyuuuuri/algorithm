n=int(input())
ugly=[0]*n
ugly[0]=1

i2=i3=i5=0
next2, next3, next5 = 2,3,5

for i in range(1,n):
    ugly[i]=min(next2, next3, next5)
    if ugly[i]==next2:
        
