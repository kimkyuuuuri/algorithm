N = int(input())
arr = list(map(int,input().split()))
q = []
ans = []

for i in range(N):
    num = i
    if not q:
        q.append(arr[i])
        ans[i] = 0
    else:
        while q[-1]<arr[i]:
            q.pop()
            num -=1
        q.append(arr[i])
        ans[i] = num
        
for i in ans:
    print(i,end=' ')
