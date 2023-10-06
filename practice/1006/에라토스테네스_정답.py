import math
n,k = map(int, input().split())
array=[True]*(n+1)
array[0]=False
array[1]=False
count=0

for i in range(2, n ):
    j=1
    while i*j<=n:
        if array[i*j]==True:
            array[i*j]=False
            
            count+=1
                
                #print(i*j)
        if count>=k:
            print(i*j)
            exit(0)
        j+=1

      
