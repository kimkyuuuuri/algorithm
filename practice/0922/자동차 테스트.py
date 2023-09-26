import sys
input=sys.stdin.readline
n,q= map(int,input().split())

array = list(map(int, input().split()))
array.sort()

for i in range(q):
    temp=int(input())
    start=0
    
    end=len(array)-1
    end_backup=end+1
    answer=0

    while  start<=end:
        mid=(start+end)//2
        if array[mid] < temp:
            start=mid+1
        elif array[mid]>temp:
            end=mid-1
        else:

            answer=(mid)*(end_backup-mid-1)
            break

    print(answer)
