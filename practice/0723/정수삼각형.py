n=int(input())
array=[]
for i in range(n):
    array.append(list(map(int,input().split())))

array[0][0]=array[0][0]

for i in range(1,n):
    for j in range(len(array[i])):
        if j==0:
            array[i][j]=array[i][j]+ array[i-1][j]
        elif j==len(array[i])-1:
            array[i][j]=array[i][j]+ array[i-1][j-1]   
        else:   
            array[i][j]=array[i][j]+max(array[i-1][j-1], array[i-1][j])

result=max(array[n-1])
    
print(result)
        
        


    
