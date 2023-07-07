n=int(input())
input_list=list(map(int,input().split()))
d=[0]*(n+1)
d[0]=input_list[0]
d[1]= max(input_list[0],input_list[1])

for i in range(3,n):
    d[i]=max(d[i-1],d[i-2]+input_list[i])

print(d[n-1])
