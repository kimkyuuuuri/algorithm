n=int(input())

#리스트 안에 튜플
array=[]
result=[]
for i in range(n):
    a,b=map(int, input().split())
    array.append([a,b])


for i in range(n):
    count=0
    for j in range(n):
        if array[j][0]>array[i][0] and array[j][1]>array[i][1]:
            count+=1
    result.append(count)
for i in range(n):
    print(result[i]+1,end=' ')
