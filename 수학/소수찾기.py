n=int(input())

array=[]
count=0
def number(num):
    if(num==1):
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i ==0:
            return False
    return True

array=list(map(int,input().split()))
for i in array:
    
    if number(i)==True:
        count+=1

print(count)
