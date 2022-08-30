import math

n=int(input())
array=[]
for i in range(n):
    array.append(int(input()))

array.sort()
print(round(sum(array)/len(array)))


if len(array)%2 !=0:
    print(array[math.trunc(len(array)/2)])
   
else:
    
    print(math.trunc(array[len(array)/2]+array[len(array)/2-1]))


arrayplus=[0]*4001
arrayminus=[0]*4001

for i in array:
    
    if i<0:
        i=-i
        arrayminus[i]+=1
        
    else:
        arrayplus[i]+=1


if max(arrayminus)>max(arrayplus):
    print(-(arrayminus.index(max(arrayminus))))
else:
    print(arrayplus.index(max(arrayplus)))
    

print(array[-1]-array[0])
