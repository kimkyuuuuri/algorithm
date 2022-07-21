n=int(input())
stack=[]
for i in range(n):
    a=input()
    
    if a=='top':
        if len(stack)!=0:
            print(stack[-1])
        else:
            print(-1)
    elif a=='size':
        print(len(stack))
    elif a=='pop':
        if len(stack)!=0:
            print(stack[-1])
            stack.pop()
        else:
            print(-1)
        
    elif a=='empty':
        if len(stack)!=0:
            print(0)
        else:
            print(1)
    else:
        
        stack.append(a.split()[1])
        
        
            
        
 
