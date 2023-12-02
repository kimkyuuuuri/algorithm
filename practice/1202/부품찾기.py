n=int(input())
array=list(map(int, input().split()))

m=int(input())
target_array=list(map(int, input().split()))
array.sort()

# binary search 정의

def binary_search(target,array):
    start=0
    end=len(array)-1
    while start<=end:
        mid=(start+end)//2
        if array[mid]<target:
            start=mid+1
        elif array[mid]>target:
            end=mid-1
        else:
            return mid
    return None
    

for i in target_array:
    result=binary_search(i, array)
    if result==None:
        print("no", end=' ')
    else:
        print("yes", end = ' ')
              
