def binary_search(start,end,times,n):
    answer=0
    while start<=end:
        mid = (start+end)//2
        people=0
        for i in times:
            people+=mid//i
        if people>=n:
            answer=mid
            end=mid-1
        elif people<n:
            start=mid+1
    return answer
 
def solution(n, times):
    answer=binary_search(1, max(times)*n , times,n)
    return answer

