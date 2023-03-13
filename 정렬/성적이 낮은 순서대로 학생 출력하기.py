n = int(input())
array=[]
for i in range(n):
    a,b = input().split()
    array.append((a, int(b)))

result = sorted(array, key=lambda x:x[1] )

#for i in range(n):
#    print(result[i][0], end=' ')

for i in result:
    print(i[0],end=' ')
