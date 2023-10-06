# 식의 결과 최대 최소

n=int(input())
array=list(map(int, input().split()))
a,b,c,d=map(int, input().split())

max_sum=-1e9
min_sum=1e9

def dfs(i,now_sum):
    global max_sum, min_sum, a,b,c,d

    if i==n:
        
        max_sum=max(max_sum, now_sum)
        min_sum=min(min_sum, now_sum)
    else:
        if a>0:
            a-=1
            new_sum=now_sum+array[i]
            dfs(i+1,new_sum)
            a+=1

        if b>0:
            b-=1
            new_sum=now_sum-array[i]
            dfs(i+1,new_sum)
            b+=1

        if c>0:
            c-=1
            new_sum=now_sum*array[i]
            dfs(i+1,new_sum)
            c+=1
            
        if d>0:
            d-=1
            new_sum=int(now_sum/array[i])
            dfs(i+1,new_sum)
            d+=1


dfs(1, array[0])
print(max_sum)
print(min_sum)

