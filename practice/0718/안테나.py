n=int(input())
array = list(map(int, input().split()))
array.sort()

if len(array)!=1:
    length=len(array)-1
    middle=length//2
    count1=0
    count2=0
    for i in array:
        count1+=abs(i-array[middle])

    for j in array:
        count2+=abs(j-array[middle+1])

    if count1>count2:
        print(array[middle+1])
    else:
        print(array[middle])
    
else:
    print(array[0])


