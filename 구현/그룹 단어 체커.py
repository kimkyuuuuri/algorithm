#구현

n=int(input())
count=0

for i in range(n):
    value=True
    array=[]
    string=input()
    array.append(string[0])
    for j in range(1,len(string)):
        
        if string[j]!=string[j-1]:
            if string[j] in array:
           
                value=False
                break
            
            array.append(string[j])
            print(array)
            

    if(value==False):
        continue
  
    count+=1
 
            
    
            

print(count)        
            
        
