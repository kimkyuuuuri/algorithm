n=int(input())

for i in range(n):
    count1=0
    count2=0
    a=input()
    result='YES'
    for j in a:
        
        if j=='(':
            count1+=1
        else:
            count2+=1
        if (count2>count1):
            result='NO'
    if(count1!=count2):
        result='NO'
    print(result)
        
