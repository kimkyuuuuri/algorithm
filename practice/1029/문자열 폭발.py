n=input()
m=input()
stack=[]
m_size=len(m)

for i in n:
    stack.append(i)
    if ''.join(stack[-m_size:])==m:
        for j in range(m_size):
            stack.pop()

answer=''.join(stack)
if answer=='':
    print('FRULA')
else:
    print(answer)
    
    
