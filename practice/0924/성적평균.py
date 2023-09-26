n,k=map(int, input().split())

array=list(map(int, input().split()))
for i in range(k):
    a,b=map(int,input().split())
    temp_sum=0
    #print(a)
    #print(b-a+2)
    for i in range(a,b+1):

        #print(array[i-1])
        temp_sum+=array[i-1]
        #print(temp_sum)
    #print(temp_sum)
    #print(b-a+1)
    print(round(temp_sum/(b-a+1),2))
        
        
