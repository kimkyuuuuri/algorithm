n=int(input())
array=list(map(int,input().split()))
number=int(input())

start,end=0,max(array)
total_budget=0

if sum(array)>=end:
    print(max(array))
    
else:
    while start<=end:
        mid=(start+end)//2
        total_budget=0
        for i in array:
            total_budget+=min(mid,i)
        if total_budget>number:
            end=mid-1
        else:
            start=mid+1
            
    print(mid)
