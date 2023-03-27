input_string=input()
num=input_string.split('-')
answer=0
for i in range(0,len(num)):
    plus=num[i].split('+')
    sum=0
    for j in plus:
        sum+=int(j)
    if (i==0):
        answer+=sum
    else:
        answer-=sum
print(answer)
