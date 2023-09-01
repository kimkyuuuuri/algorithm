import sys
input= sys.stdin.readline
n,m = map(int, input().split())
number=input()

count=0
number_array=list(number)
stack = [number_array[0]]
for i in range(len(number)-1):
    if not number_array[i].isdigit():
        break
    i_number = int(number_array[i])
    while stack and int(stack[-1])<i_number :
        stack.pop()
        count+=1
        if count>m:
            for j in range(i,len(number)-1):
                j_number = number_array[j]
                stack.append(j_number)
            print(''.join(stack))
            exit(0)
            break
    stack.append(number_array[i])
print(stack)

#런타임 에러 
    
        
