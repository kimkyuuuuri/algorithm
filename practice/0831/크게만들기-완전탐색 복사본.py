import sys
input= sys.stdin.readline
n,m = map(int, input().split())
number=input().rstrip()

count=0
stack=[]

for i in range(len(number)):
    while stack and stack[-1] < number[i] :
        stack.pop()
        count+=1
        if count>m+1:
            stack.append(number[i:])
            print(''.join(stack))
            exit(0)
    stack.append(number[i])
print(''.join(stack))

# 런타임 에러
# 문자열이라도 그냥 비교할 수 있음. 
