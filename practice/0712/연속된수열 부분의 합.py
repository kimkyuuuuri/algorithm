def solution(sequence, k):
    answer = []
    sum=0
    start=0
    end=0
    answer.append(0)
    answer.append(1000000)
  
    prefix_sum=[0]
    for i in range(len(sequence)):
        sum+=sequence[i]
        prefix_sum.append(sum)
        if sum>=k and end==0:
            end=i+1
  
    while start<=end and end<=len(prefix_sum)-1 :
       
        if prefix_sum[end]-prefix_sum[start] == k:
            
            if answer[1]-answer[0]+1 > end-start:
                answer[0]=start+1
                answer[1]=end
              
            start+=1
            end+=1
          
        elif prefix_sum[end]-prefix_sum[start] < k :
            end+=1
        else:
            start+=1
 
    answer[0]-=1
    answer[1]-=1
    return answer
               
            
              
            

