n=input()
array=list(n)
index=len(n)
m=int(input())

for i in range(m):
    a=input()
    temp=a.split(' ')
    if temp[0]=='P':
        array.insert(index, temp[1])
        index+=1
    elif temp[0]=='L':
        if index!=0:
            index-=1
    elif temp[0]=='D':
        if index<=len(array):
            index+=1
    else:
        if index!=0 and index < len(array):
            index-=1
            array.pop(index)
        elif index ==len(array):
            index-=1
            array.pop(index)
        


print(''.join(array))
