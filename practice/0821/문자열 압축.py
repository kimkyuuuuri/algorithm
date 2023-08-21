def solution(s):
    answer=len(s)
    for i in range(1, len(s)//2+1):
        array=''
        count=1
        index=0
        while index<=len(s):
            if s[index:index+i]==s[index+i:index+i+i]:
                count+=1
            else:
                if count!=1:
                    array+=str(count)
                count=1
                array+=s[index:index+i]
            index+=i 
        answer=min(answer,len(array))
    return answer
