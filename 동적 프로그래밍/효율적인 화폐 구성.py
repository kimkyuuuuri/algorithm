n,m=map(int(input().split()))
array=[]
for i in range(n):
    array.append(int(input()))

d=[10001] *(m+1)

d[0]=0
for i in range(n):
    #화폐 단위를 확인
    for j in range(array[i],m+1):
        #금액을 확인
        if d[j-array[i]]!=10001 :
            d[j]=min(d[j],d[j-array[i]]+1)

if d[m]==10001:
    print(-1)
else:
    print(d[m])

    
