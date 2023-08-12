def solution(n):
    
    result_array=[]
    result_mul=0
    
    for i in range(2, 10):
        num=n
        result=1
        array=[]
        while num >=i :
            a=num%i
            num=num//i
            array.append(a)
            
            if a!=0:
                result*=a
                
        array.append(num)
        result*=num
        array=list(reversed(array))

        if result_mul < result:
            result_mul = result
            result_array=array
            
    return result_array
   
print(solution(13))
