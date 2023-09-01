import sys
input= sys.stdin.readline
array=[]
answer=0
n=int(input())
for i in range(n):
    a,b = map(int, input().split())
    array.append([a,b])

array.sort(key = lambda x:(x[1],x[0]))
temp=0
for i in array:
    if temp <= i[0]:
        answer+=1
        temp=i[1]
print(answer)
        
    
