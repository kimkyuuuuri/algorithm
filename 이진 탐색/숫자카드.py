n=int(input())
array=list(map(int, input().split()))
m=int(input())
targetlist=list(map(int,input().split()))
lastresult=[]

array.sort()
def binary_search(array, target,start,end):
    if start > end:
        return None

    mid =(start+end)//2
    if array[mid]==target:
        return mid
    elif array[mid] >  target:
        return binary_search(array,target,start,mid -1)
    else:
        return binary_search(array, target, mid+1, end)

for i in targetlist:
    result=binary_search(array,i,0,n-1)
    if result==None:
        lastresult.append(0)
    else:
        lastresult.append(1)

for i in lastresult:
    print(i,end=' ')
