n=int(input())
#공은 그대로이고 컵의 위치가 계속 변경됨
# 상황을 그려보면
# 반복문으로 그냥 다 돌려보면 되려나?
#최종적으로 나와야하는건 1번 위치에 어떤 컵이 있을까 -> 배열로 생각하면 되겠는데?
array=[1,2,3]

for i in range(n):
    ninput=list(map(int,input().split()))
    #map의 용도가 뭐지?
    
    array[ninput[0]-1], array[ninput[1]-1] = array[ninput[1]-1], array[ninput[0]-1]

print(array[0])

#현재 오류남
