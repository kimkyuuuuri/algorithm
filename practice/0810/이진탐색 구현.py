def binary_search(array, target):
    start = 0
    end = len(array)-1
    mid = (start+end)//2

    while start<=end:
        if array[mid] < target:
            start=mid+1
        elif array[mid]>target:
            end=mid-1
        else:
            return mid

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target)
if result == None:
    print("원소존재 X")
else:
    print(result+1)
    
    
