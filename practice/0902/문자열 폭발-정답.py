n=input()
m=input()
stack = []
index = len(m)

for i in n:
    stack.append(i)
    if stack[-len(m):]==list(m):
        for j in range(len(m)):
            stack.pop()

if len(stack)==0:
    print('FRULA')
else:
    print(''.join(stack))




