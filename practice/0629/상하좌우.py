# R= (1,0)
# L= (-1,0)
# U= (0,1)
# D= (0,-1)

n= int(input())
arr = list(input().split())
start = [1,1]

for i in range(len(arr)):
    if arr[i]=='R' and start[0]<n:
        start[0]=start[0]+1
    elif arr[i]=='L' and start[0]>1:
        start[0]=start[0]-1
    elif arr[i]=='U' and start[1]>1:
        start[1]=start[1]-1
    elif arr[i]=='D' and start[1]<n:
        start[1]=start[1]+1
        
print(start[1],start[0])
