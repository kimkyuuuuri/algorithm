import sys
n=int(sys.stdin.readline())
array=[]
for i in range(n):
    age, name = input().split()
    array.append((int(age), name, i))
array.sort(key=lambda x:(x[0], x[2]))

for i in array:
    print(i[0],end =' ')
    print(i[1])

