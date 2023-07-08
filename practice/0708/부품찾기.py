def binary_search(array, target, start, end):
    while start<=end:
        mid= (start+end)//2
        if array[mid]<target:
            start=mid+1
        elif array[mid]>target:
            end=mid-1
        else:
            return mid
    return None
            

n = int(input())
arrayn = list(map(int, input().split()))
m = int(input())
arraym = list(map(int, input().split()))

print(arrayn)
print(arraym)
arrayn.sort()

result=0
for i in range(m):
   
    result =  binary_search(arrayn, arraym[i],0,n-1)
    if result == None:
        print("no")
    else:
        print("yes")

    
        
