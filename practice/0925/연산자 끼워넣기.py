n=int(input())
num_array = list(map(int, input().split()))
#plus, sub, mul, div = map(int, input().split())

plus_array = list(map(int, input().split()))
answer_list=[]
def dfs(now, count,plus_array):
    if count==n:
        answer_list.append(now)
        return

    if plus_array[0]!=0:
        plus_array[0]-=1
        dfs(now+num_array[count],count+1, plus_array)
        plus_array[0]+=1

    if plus_array[1]!=0:

        plus_array[1]-=1
        dfs(now-num_array[count],count+1, plus_array)
        plus_array[1]+=1

    if plus_array[2]!=0:
        
        plus_array[2]-=1
        dfs(now*num_array[count],count+1, plus_array)
        plus_array[2]+=1
    
    if plus_array[3]!=0:
        plus_array[3]-=1
        dfs(int(now/num_array[count]),count+1, plus_array)
        plus_array[3]+=1
        

dfs(num_array[0],1,plus_array)
answer_list.sort()

print(answer_list[-1])
print(answer_list[0])
