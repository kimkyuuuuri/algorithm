A, B, V = map(int,input().split())
# map은
# 오답 

oneday=A-B
totalday=V//oneday
totalday-=1

if V%oneday==0:
        totalday+=1


if (totalday-1)*oneday+A>=V:
        totalday-=1
print(totalday)


total=0
result=0

#반복문 사용
for i in range(totalday):
        total+=A
        result+=1
        if total>=V:
                break
        total-=B
        
print(result)


        

