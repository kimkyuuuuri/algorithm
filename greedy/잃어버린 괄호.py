import re
a=input()
numbers=re.findall(r'\d+',a)
array=[]
num=[]

for i in a:
    if i=='-' or i=='+':
        array.append(i)


for i in range(len(array)):
    if array[i]=='+':
        numbers[i+1]=int(numbers[i])+int(numbers[i+1])                             
        numbers[i]=0

while 0 in numbers:
    numbers.remove(0)
    
result=int(numbers[0])*2

for i in numbers:
    result-=int(i)

print(result)
      
        
    
        
        
