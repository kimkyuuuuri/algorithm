# 직접 작성한 코드
n,k=map(int,input().split())
array=[]
for i in range(2):
    array.append(list(map(int, input())))


array[0].sort()
array[1].sort()

print(array[0])
print(array[1])
total=sum(array[0])

for i in range(k):
    if array[0][i]<array[1][n-i-1]:
        total=total-array[0][i]+array[1][n-i-1]

print(total)


#답안

n,k=map(int, input().split())
a=list(map(int, input().split()))
b=list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
	if a[i]<b[i]:
    	a[i],b[i],b[i],a[i]
    else:
    	break
print(sum(a))
