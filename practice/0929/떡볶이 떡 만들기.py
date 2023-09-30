n,m = map(int, input().split())
array = list(map(int, input().split()))
array.sort()

def binary_search(m,array):
    start=0
    end=array[-1]

    answer=0
    while start<=end:
        mid=(start+end)//2
        temp=0
        for i in array:
            if i>mid:
                temp+=i-mid

        if temp<m:
            end=mid-1
        elif temp>=m:
            start=mid+1
            answer=mid

    return answer

answer= binary_search(m,array)
print(answer)
            
       
    
    
