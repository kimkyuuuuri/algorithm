n=input()

array=list(n)

result=0
count=0
for i in range(1,len(array)):
    if array[i]!=array[i-1]:
        count+=1

    if count%2==0:
        result=count//2
    else:
        result=count//2+1
        
print(result)
