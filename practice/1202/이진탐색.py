def binary_search(array, target):
    start=0
    end=len(array)
    while start<=end:
        mid = (start+end)//2
        if array[mid]>target:
            end=mid-1
        elif array[mid]<target:
            start=mid+1
        else:
            return mid

    return None

n, target = map(int, input().split())
array = list(map(int, input().split()))

result = binary_search(array, target)
if result == None:
    print("원소가 존재하지 않습니다")
else:
    print(result+1)

