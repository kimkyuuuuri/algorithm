def dfs(now_index, now_sum, numbers):
    global answer_list
    if now_index==len(numbers):
        answer_list.append(now_sum)
        return 
    
    dfs(now_index+1, -numbers[now_index]+now_sum, numbers)
    dfs(now_index+1, numbers[now_index]+now_sum, numbers)
        
def solution(numbers, target):
    global answer_list
    answer_list=[]
    answer=0   
    dfs(0,0,numbers)
    for i in answer_list:
        if i==target:
            answer+=1

    return answer 
