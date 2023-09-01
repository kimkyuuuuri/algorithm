n=input()
stack=[n[0]]
count=0
answer=0

for i in range(1, len(n)):
    if n[i]==')' and n[i-1]=='(':
        stack.pop()
        answer+=len(stack)
    elif n[i]=='(':
        stack.append('(')
    elif n[i]==')':
        stack.pop()
        answer+=1

print(answer)        
    
         
    
    
