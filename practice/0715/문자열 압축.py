def solution(s):
    result=len(s)
    index=0
    num_array=[]
    for i in range(1,len(s)//2+1):
        n_count=len(s)
        first_check=0
        num=0
        test=[]
        while index+i<len(s):
            if s[index:index+i] == s[index+i:index+2*i]:
                num+=1
                if first_check==0:
                    
                n_count-=i
                first_check=1
            else:
                if num!=0:
                    num_array.append(len(str(num+1)))
                num=0
                first_check=0
            index+=i
        if num!=0:
            num_array.append(len(str(num+1)))
          
        index=0
        n_count+=sum(num_array)
        num_array.clear()
        result=min(result, n_count)
       
    answer = result
    return answer
