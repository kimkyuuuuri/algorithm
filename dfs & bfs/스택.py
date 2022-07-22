n=int(input())
stack=[]
for i in range(n):
    a=input()
    if a.split()[0]=='push':
        stack.append(a.split()[1])
        
        
    elif a=='top':
        if not stack:
            print(-1)
        else:
            print(stack[-1])
    elif a=='size':
        print(len(stack))
    elif a=='pop':
        if not stack:
            print(-1)
        else:
            print(stack[-1])
            stack.pop()
           
    elif a=='empty':
        if not stack:
            print(1)
        else:
            print(0)
   
        
        
        
            
        
 
