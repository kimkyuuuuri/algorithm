import sys
input=sys.stdin.readline
n,c = map(int, input().split())

# 인접한 두 공유기 사이의 거리가 최대
# 범위가 너무 크네? 이분 탐색을 사용할 수 있을까?
# 하나 하나 사이의 최대 거리를 mid와 비교한다. 
array=[]

for i in range(n):
    array.append(int(input()))
    
array.sort()

start=1
end=array[-1]-array[0]
answer=0

while start<=end:
    mid=(start+end)//2
    value=array[0]
    count=1

    for i in range(1,n):
        if array[i]>=value+mid:
            value=array[i]
            count+=1
            
    if count>=c:
        start=mid+1
            # 값 저장하기 
        answer=mid
    else:
        end=mid-1
        
print(answer)
        

    # 만약에 감당 가능하다면 일단 answer에 저장
    
