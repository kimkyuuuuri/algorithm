n=input()
result=1
array=[]
array.append(n[0])

for i in range(1,len(n)):
    if n[i] in array :
        if n[i]=='6' and array.count('6')> array.count('9'):
            array.append('9')
            continue
                
        elif n[i]=='9' and array.count('9')> array.count('6') :
            array.append('6')
            continue
            
        result+=1
    array.append(n[i])
    
    
print(result)
