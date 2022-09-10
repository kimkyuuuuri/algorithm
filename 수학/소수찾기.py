n=int(input())

#소수 어떻게 구하더라
#일단 제곱근까지만 구하면 됨
#자신보다 작은수를 탐색하면서 몫 있으면 탈락
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
