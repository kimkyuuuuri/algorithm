n=int(input())
n=1000-n

array=[500,100,50,10,5,1]
count=0

for i in array:
    count+=n//i
    n%=i

print(count)



