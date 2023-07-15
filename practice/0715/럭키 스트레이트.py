n=input()
array=list(map(int,n))
print(n[0])

half=len(array)//2
left_count=0
right_count=0
for i in range(half):
    left_count+=array[i]
    right_count+=array[len(array)-i-1]

if left_count==right_count:
    print("LUCKY")
else:
    print("READY")


    
