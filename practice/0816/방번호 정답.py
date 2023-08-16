n=input()
array=[0]*10
result=0
for i in n:
    if i=='6' or i=='9':
        if array[6]<array[9]:
            array[6]+=1
        else:
            array[9]+=1
    else:
        array[int(i)]+=1

for i in range(10):
    result=max(result, array[i])

print(result)


