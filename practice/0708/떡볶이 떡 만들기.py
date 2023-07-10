def binary_search(array, target, start, end):
    # 계산 식
    count=0
    if start>end:
        return None
  
    mid=(start+end)//2
    for i in range(len(array)):
        count+=max(0,array[i]-mid)
    
    if count>target:
        return binary_search(array,target,mid+1,end)
    elif count<target:
        return binary_search(array,target,start,mid-1)
    else:
        return mid

n,m = map(int, input().split())
array = list(map(int, input().split()))
array.sort()
result=binary_search(array,m,0,array[-1])
    
print(result)
