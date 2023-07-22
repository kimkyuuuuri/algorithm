# 재귀로 구현 
def bisect_left(target,x,start,end):
    if start>end:
        return None

    mid=(start+end)//2

    # 같을 때
    if (mid == 0 or x[mid-1]<target) and x[mid]==target:
        return mid
        
    # 더 작을 때
    elif x[mid]<target:
        return bisect_left(target,x,mid+1, end)
    else:
        return bisect_left(target,x,start,mid-1)


# 재귀로 구현 
def bisect_right(target,x,start,end):
    if start>end:
        return None
    
    mid=(start+end)//2

    # 같을 때
    if (mid == n-1 or x[mid+1]>target) and x[mid]==target:
        return mid
        
    # 더 작을 때
    elif x[mid]<=target:
        return bisect_right(target,x,mid+1, end)
    else:
        return bisect_right(target,x,start,mid-1)
    # 더 클 때

def  count(array,x):
    left_index=bisect_left(x, array, 0, len(array)-1)
    right_index=bisect_right(x, array,0,len(array)-1)
    if left_index==None:
        return 0

    return (right_index-left_index+1)


n,x = map(int, input().split())
array=list(map(int, input().split()))

result= count(array,x)
if result ==0:
    print(-1)
else:
    print(result)




    
    
