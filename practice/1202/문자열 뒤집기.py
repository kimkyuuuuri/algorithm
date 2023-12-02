n=input()

# case1: 모두 1으로 바꾸기
# case2: 모두 0으로 바꾸기 
case1=0
case2=0

for i in range(len(n)-1):
    if (n[i]=='0' and n[i+1]=='1'):
        case1+=1
if n[len(n)-1]==0:
    case1+=1


for i in range(len(n)-1):
    if n[i]=='1' and n[i+1]=='0':
        case2+=1
        case1+=1
if n[len(n)-1]==1:
    case2+=1

print(case1)
print(case2)
