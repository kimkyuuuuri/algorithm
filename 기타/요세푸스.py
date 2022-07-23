n,k=map(int,input().split())
array=[]
result=[]
index=0
for i in range(n):
    array.append(i+1)
print(array)

for i in range(n):
    index+=k-1
    index=index%len(array)
    result.append(array.pop(index))

print('<',end='')
for i in range(n):
    print(result[i],end='')
    if i==n-1:
        break
    print(', ', end='')
print('>',end='')
