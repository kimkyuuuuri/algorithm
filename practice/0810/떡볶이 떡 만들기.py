def binary_search(array, target):
    start=1
    end=max(array)
    answer=0

    while start<=end:
        mid=(start+end)//2
        result=0
        for i in array:
            if i>mid:
                result+=i-mid
                
        if result<target:
            end=mid-1
    
        else:
            answer=mid
            start=mid+1
            
    return answer
    
    


n, m = map(int, input().split())
array = list(map(int, input().split()))
print(binary_search(array,m))
