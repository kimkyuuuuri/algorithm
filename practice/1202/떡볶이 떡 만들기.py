n,m = map(int, input().split())
array = list(map(int, input().split()))
 

def binary_search(target, array, end):
    start=0
    result=0
    while start<=end:
        mid=(end+start)//2
        dduck=0
        for i in array:
            dduck+=max(0, i-mid)
        if dduck < target:
            end=mid-1
        else:
            result=mid
            start=mid+1
    return result
    
print(binary_search(m, array, max(array)))
              
