n,m=map(int,input().split())
array=[]
array2=[]
count=0
for i in range(n):
    nn=input()
    array.append(nn)


for i in range(m):
    mm=input()
    if mm not in array:
        continue
    else:
        count+=1
print(count)

    
    
