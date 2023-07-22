def bisect(array, start,end):
    mid=(start+end)//2
    if start>end:
        return -1
    if array[mid]==mid:
        return mid
    if array[mid]<mid:
        return bisect(array, mid+1, end)
    else:
        return bisect(array, start, mid-1)
        
        
        
n=int(input())
array=list(map(int, input().split()))

index=bisect(array,0, n-1)
print(index)
