#직접 작성한 코
n,m=map(int,input().split())

array=list(map(int, input().split()))
array.sort()
num=array[-1]-1

for i in range(m):
    count=0
    for j in array:
        if j<=num:
            continue
        else:
            count+=j-num
    
    if count==m:
        break
    num-=1

print(num)

#답
start=0
end=max(array)

while(start<=end):
	total=0
    mid=(start+end)//2
    for x in array:
    	if x>mid:
        	total+=x-mid
    if total<m:
    	end=mid-1
    else:
    	result=mid
        start=mid+1

print(result)   
    


    
