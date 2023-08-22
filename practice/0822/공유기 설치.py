import sys
input=sys.stdin.readline
n,k = map(int, input().split())
array=[]

for i in range(n):
    array.append(int(input()))

array.sort()

# 거리를 기준으로 한다. 
start=1
end = array[-1]-array[0]
answer=0
#0은 설치되어 있다는 가정하에 진행 

while start<=end:
    count=1
    value=array[0]
    mid = (start+end)//2
    # 최소 거리를 뜻함 
    for i in range(1,n):
        if array[i] >= value + mid:
            count+=1
            value = array[i]
    if count >= k:
        start=mid+1
        answer=mid

    else:
        end  = mid-1
print(answer)
            
    
        
        
