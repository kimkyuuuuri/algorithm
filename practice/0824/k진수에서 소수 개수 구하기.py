import math
def fc(x):
    if x==1 or x==0:
        return False
    else:
        for i in range(2, int(math.sqrt(x))+1):
            if x%i==0:
                return False
    return True
    
    
def solution(n, k):
    answer = 0
    k_number =''
    back_up=n
    while n>=k:
        temp=n%k
        n//=k
        k_number = str(temp)+k_number
    k_number=str(n)+k_number
   
    array = k_number.split('0')
    for i in array:
        if i != '' and fc(int(i)):
            answer+=1
    
    return answer
