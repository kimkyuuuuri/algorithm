n = int(input())


d = [[0]*(n+1)]*(n+1)
arr = []

for i in range(n):    
	arr.append(list(map(int, input().split())))
d=arr

 
for i in range(1,n):
    d[i][0]=min(d[i-1][0],d[i][0])
    d[0][i]=min(d[0][i-1],d[0][i])


for i in range(1,n):
    for j in range(1,n):
        d[i][j]=min(max(d[i-1][j],d[i][j-1]),d[i][j])

print(d[n-1][n-1])

