n=int(input())
array=list(map(int, input().split()))
b,c = map(int, input().split())
result=0

for i in array:
    i-=b
    result+=1
    if i>0:
        result+=i//c
        if i%c !=0:
            result+=1

print(result)
