import sys
input_array=list(sys.stdin.readline())
count=0
stack=[]
count2=0
for i in range(len(input_array)):
    stack.append(input_array[i])
    if input_array[i]==")":
        stack.pop()
        stack.pop() 
        if input_array[i-1]=="(":
            if(len(stack)>0):
                count+=len(stack)
        else:
            count2+=1
    
print(count2+count)

