from collections import deque
def solution(priorities, location):
    answer = 0
    array=list(enumerate(priorities))
    que=deque(array)
    while que:
        now=que.popleft()
        if que and now[1] < max(que, key =lambda x:x[1])[1]:
            que.append(now)  
        else:
            answer+=1
            if now[0]==location:
                break

    return answer
