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
        if i=='[' or i==']' or i=='(' or i==')':
            dq.append(i)
            
    for i in range(math.floor(len(dq)/2)):
        
        st=dq.pop()
        
        if(dq[-1]=='[' and st==']'):
            dq.pop()
            
            continue
        elif(dq[-1]=='(' and st==')'):
            dq.pop()
        
            continue
        
        elif(dq[-0]=='[' and st==']'):
            dq.popleft()
            
          
            continue
        elif(dq[-0]=='(' and st==')'):
            dq.popleft()
         
            continue
        else:
            
            result='no'
        if len(dq)==0:
            break
        
            
    
    if(len(dq)!=0):
        result='no'
    print(result)
      
   

#(([ (([( [ ] ) ( ) (( ))] )) ]). 해결 안됨

#닫는 괄호를 만나면 안에 있는 모든것을 빼는 방법은?
