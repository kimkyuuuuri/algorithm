import math

n=int(input())
array=[]
arrayplus=[0]*8002
for i in range(n):
    array.append(int(input()))

array.sort()
print(round(sum(array)/len(array)))

index=n/2
if n%2 !=0 :
    print(array[math.trunc(n/2)])


for i in array:
    
    if i<0:
        i=(-i)+4001
        arrayplus[i]+=1
        
    else:
        arrayplus[i]+=1


#음수인 케이스 예외처리 해줘야함
#출력이 안될때가 있음.

m=max(arrayplus)
arrayresult=[]
count=0
for i,v in enumerate(arrayplus):
    if v==m:
        arrayresult.append(i)




if len(arrayresult)<2:
    print(arrayresult[0])
    
else:
    print(arrayresult[1])

    
    

    

    
print(array[-1]-array[0])
