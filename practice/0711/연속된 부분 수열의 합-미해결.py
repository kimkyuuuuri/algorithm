def solution(sequence, k):
    answer = []
    count=0
    index=0

    for i in range(1,len(sequence)+1):
        #print(sequence[-1-i:len(sequence)])
        if sum(sequence[len(sequence)-i:len(sequence)])<k:
            continue
            
        # i는 갯수 
        # 최적화 
        start = 0
        end = len(sequence)-i+1
       
        while True:
            mid = (start+end)//2
       # for j in range(0,len(sequence)-i+1):
            count=sum(sequence[mid:mid+i])
            if count<k:
                start=mid
            elif count>k:
                end=mid
            else:
                answer.append(mid)
                answer.append(mid+i-1)
                return answer
                break
        
        while True:
            mid-=1
            count=sum(sequence[mid:mid+i])
            if count==k:
               
                answer[0]=mid
                answer[1]=mid+i-1
            else:
                return answer
               
        return answer
               
            
              
            

