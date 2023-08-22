n=int(input())
array=list(map(int,input().split()))
k = int(input())
sum_array = sum(array)
if sum_array <= k:
    answer=max(array)
    print(answer)
    
else:
    start=0
    end=max(array)
    answer=0
    
    while start<=end:
        # 잘라지는 커트 기준
        temp=0
        mid = (start+end)//2
        for i in array:
            if i>=mid:
                temp+=mid
            else:
                temp+=i
        if temp > k :
            end = mid -1
            #answer = mid 
        else :
            start = mid + 1
            
            
    
    print(end)
        
        
        


