n=int(input())
array=[]
array.append(0)
array.append(1)
for i in range(n+1):
    if i==0 or i==1 :
        continue
    array.append(array[i-1]+array[i-2])

print(array[n])
