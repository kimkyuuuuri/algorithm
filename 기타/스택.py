import sys
num=int(sys.stdin.readline())
stack=[]
for _ in range(num):
    input_list=list(sys.stdin.readline().split())
   
    if input_list[0]=='push':
        stack.append(int(input_list[1]))
    elif input_list[0]=='pop':
        if(len(stack)==0):
            print(-1)
        else:
            print(stack[-1])
            stack.pop()
    elif input_list[0]=='size':
        print(len(stack))
    elif input_list[0]=='empty':
        if(len(stack)==0):
            print(1)
        else:
            print(0)
    elif input_list[0]=='top':
        if(len(stack)==0):
            print(-1)
        else:
            print(stack[-1])
 
        
        
