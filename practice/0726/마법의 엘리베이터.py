
def fibo(storey,d):
    answer = 0
    num=storey
    if num<10:
        if num > 5:
            return 11-num
        else:
            return num
    if d[num]!=0:
        return d[num]
    
    print("Test")
    print(fibo(d[num//10+1],d))
    print(fibo(d[num//10],d))
    print(d[num%10])
    d[num]= min(fibo(d[num//10+1],d) , fibo(d[num//10],d) ) + d[num%10]
   
    return d[num]
  
def solution(storey):
    
    d=[0]*100000001
    for i in range(1,11):
        if i<5:
            d[i]=i
        else:
            d[i]=11-i
            
    answer=fibo(storey,d)
    
    return answer
