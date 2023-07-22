
def solution(N, stages):
    answer = []
    array=[0]*(max(stages)+1)
    result=[]
    count=0
    num=len(stages)
    for i in stages:
        array[i]+=1
    
    for i in range(1,N+1):
        result.append([i,array[i]/num])
        num-=array[i]
 
    result.sort(key=lambda x:x[1], reverse=True)
    
    if len(stages)==0:
        answer.append(0)
    else:
        
    
        for i in result:
            answer.append(i[0])
    
    return answer
