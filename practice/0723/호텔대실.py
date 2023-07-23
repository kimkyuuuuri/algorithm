import heapq
def solution(book_time):
    answer = 1
    book_time.sort()
    q=[]

    end_time=int(book_time[0][1].split(":")[0])*60 + int(book_time[0][1].split(":")[1])
    heapq.heappush(q,end_time)
    
    for i in range(1,len(book_time)):
        start_time=int(book_time[i][0].split(":")[0])*60 + int(book_time[i][0].split(":")[1])
        end_time=int(book_time[i][1].split(":")[0])*60 + int(book_time[i][1].split(":")[1])
        
        if start_time < q[0]+10:
            answer+=1
        else:
            heapq.heappop(q)  

        heapq.heappush(q,end_time)
   
    return answer
