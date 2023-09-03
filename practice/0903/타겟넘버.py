def solution(numbers, target):
    global answer
    answer=0   
    dfs(0,0,target,numbers)
    return answer 

def dfs(sum_value,index,target,numbers):
        global answer
        if sum_value==target and index==len(numbers):
            answer+=1
            return
        if index>len(numbers)-1:
            return
        dfs(sum_value+numbers[index],index+1, target, numbers)
        dfs(sum_value-numbers[index],index+1, target, numbers)
        
