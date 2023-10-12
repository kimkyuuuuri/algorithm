n=int(input())
array=list(map(int, input().split()))
a,b,c,d=map(int, input().split())
global answer_list
answer_list=[]

def dfs(i,now_sum):
    global a,b,c,d
    if i==len(array):
        answer_list.append(now_sum)
        return 

    if a>0:
        a-=1
        new_sum=now_sum+array[i]
        dfs(i+1, new_sum)
        a+=1
    if b>0:
        b-=1
        new_sum=now_sum-array[i]
        dfs(i+1, new_sum)
        b+=1

    if c>0:
        c-=1
        new_sum=now_sum*array[i]
        dfs(i+1, new_sum)
        c+=1

    if d>0:
        d-=1
        new_sum=now_sum/array[i]
        dfs(i+1, int(new_sum))
        d+=1
        
dfs(1,array[0])
print(max(answer_list))
print(min(answer_list))
    
    
        
        
    
