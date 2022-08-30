import math

n=int(input())
array=[]
arrayplus=[0]*4001
arrayminus=[0]*4001
for i in range(n):
    array.append(int(input()))

array.sort()
print(round(sum(array)/len(array)))

index=n/2
if n%2 !=0 :
    print(array[math.trunc(n/2)])


for i in array:
    
    if i<0:
        i=-i
        arrayminus[i]+=1
        
    else:
        arrayplus[i]+=1


#여기까지 배열 잘 만들었음
#두번째로 작은 값 찾아야 해 ..을 enumerate 이
#문제 1) 모두 음수일 떄, 모두 양수일 때 최대값이 0이기 때문에 루프를 많이 돔
#둘다 있을 때 두번째 수를 찾는 방법이 어려움.. 

m1=max(arrayminus)
m2=max(arrayplus)
for i,v in enumerate(arrayminus):
    if v==m1:
        print(i,v)
        print("얘는 마이너스")
for i2,v2 in enumerate(arrayplus):
    if v2==m2:
    
        print(i2,v2)
        print("얘는 플러스")

        
if max(arrayminus)>max(arrayplus):
    print(-(arrayminus.index(max(arrayminus))))
else:
    print(arrayplus.index(max(arrayplus)))
    

print(array[-1]-array[0])
