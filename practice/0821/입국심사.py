def binary_search(n, times):
    start=1
    end=max(times)*n
    answer=0
    
    while start<=end:
        temp=0
        mid = (start+end)//2 
        for i in times:
            temp+=mid//i
   
        if temp >= n:
            answer=mid
            end=mid-1
        
        else: 
            start=mid+1
    return answer

def solution(n, times):
    answer= binary_search(n,times)
    return answer
