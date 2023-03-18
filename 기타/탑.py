import sys
num=int(sys.stdin.readline())
input_list=list(sys.stdin.readline().split())
stack=[]
#index 대신 갯수 count

for i in range(num):
    for j in range(i):
        if input_list[i]<=input_list[j]:
            input_list.pop()
            stack.append(j+1)
            break
        if j==0:
            stack.append(0)
stack.append(0)


print(" ".join(map(str, stack[])))


        
        
