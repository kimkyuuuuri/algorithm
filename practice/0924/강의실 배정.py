import sys
input=sys.stdin.readline
n = int(input())
array=[]
for i in range(n):
    a,b=map(int, input().split())
    array.append([a,b])

array.sort(key=lambda x:x[1])
count=1
stack=[array[0][1]]

for i in range(1,n):
    if stack[0]<=array[i][0]:
        count+=1
        stack.pop()
        stack.append(array[i][1])
print(count)
        
    
    
