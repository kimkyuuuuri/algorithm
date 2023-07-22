def solution(x, y, n):
    answer = 0
    # 무조건 작다고 좋은 것은 아님.
    while True:
       
        if (y%2==0 and y//2 ==x) or (y%3==0 and y//3 ==x) or y-n==x:
            return answer+1
        
        num_1=y%3
        num_2=y%2
        num_3=y-n
        
        if num_1==0:
            if num_3 < y//3:
                y=num_3
            else:
                y=y//3
            
        elif num_2==0:
            if num_3<y//2:
                y=num_3
            else:
                y=y//2
        else:
            y=y-n  
        answer+=1
        if x==y:
            return answer
            
        elif y<x:
            return -1
    return answer
