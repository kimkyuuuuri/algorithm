n=int(input())
array_t=[0]
array_p=[0]
answer_array=[]

for i in range(n):
    a,b = map(int, input().split())
    array_t.append(a)
    array_p.append(b)

# 넣고 뺴꼬 

def dfs(now_day, i , now_sum, array):
    global answer_array
    for j in range(i, n+1):
        if array_t[j]+j<=n+1 and now_day<=j and j not in array:
            array.append(j)
            dfs(array_t[j]+j,j,now_sum+array_p[j], array)
            array.pop()

        elif array_t[j]+j>n+1 or j==n  :
           
            answer_array.append(now_sum)
            return
        
    
    
dfs(0,1,0,[])
print(max(answer_array))
        
    
