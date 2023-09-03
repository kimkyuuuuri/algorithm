import sys
input=sys.stdin.readline
n=input().rstrip()
array=list(n)
index=len(n)
m=int(input().rstrip())
stack_l=array
stack_r=[]

for i in range(m):
    a=input().rstrip()
    temp=a.split(' ')
    if temp[0]=='P':
        stack_l.append(temp[1])
    elif stack_l and temp[0]=='L':
        stack_r.append(stack_l.pop())
    elif stack_r and temp[0]=='D':
        stack_l.append(stack_r.pop())
    elif stack_l and temp[0]=='B':
        stack_l.pop()
           

result_stack_r = list(reversed(stack_r))
result=stack_l+ result_stack_r
# 스택을 쓰는 이유는 append, pop 연산을 쓰기 위함 ! 
print(''.join(result))

