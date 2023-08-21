n=int(input())
array_hole=set(map(int, input().split()))

m=int(input())
array_set=list(map(int, input().split()))


for i in array_set:
    if i in array_hole:
        print("yes", end=' ')
    else:
        print("no", end=' ')
        
        
    
