from collections import deque
import math

while True:
    array=[]
    a=list(input())
    dq=deque()
  
    
    result='yes'
    if a[0]=='.' and len(a)==1:
        break
    for i in a:
        
        if i=='[' or i== '(':
            dq.append(i)
            
        elif i==']':
            if len(dq)==0:
                result='no'
                break
            st=dq.pop()
            
            if st!='[':
                result='no'
                break
            
        elif i==')':
            if len(dq)==0:
                result='no'
                break
            st=dq.pop()
            if st!='(':
                result='no'
                break
            
        
   
    if (len(dq)!=0):
        result='no'
    print(result)
      
   

#(([ (([( [ ] ) ( ) (( ))] )) ]). 해결 안됨

#닫는 괄호를 만나면 안에 있는 모든것을 빼는 방법은?
