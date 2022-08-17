#재귀 함수 호출하는 건데, 배열을 이용해서 한번 구한 내용은 더이상 구하지 않도록 하는 것이 핵심 !
#문제는 어떤 배열을 선언해야하지?

def w(a,b,c):
    global array
    if a<=0 or b<=0 or c<=0:
        return 1
    elif a>20 or b>20 or c>20:
        print(1)
        print(array[a][b][c])
        return array[a][b][c]
    elif a<b and b<c:
        array[a][b][c]=array[a][b][c-1]+array[a][b-1][c-1]-array[a][b-1][c]
        print(2)
        print(array[a][b][c])
        return array[a][b][c]
    else:
        array[a][b][c]=array[a-1][b][c]+array[a-1][b-1][c]+array[a-1][b][c-1]-array[a-1][b-1][c-1]
        print(3)
        print(array[a][b][c])
        return array[a][b][c]

while True:
    inputa,inputb,inputc = map(int,input().split())
    array = [[[0 for x in range(50)] for j in range(50)] for i in range(50)]
    
    if inputa==-1 and inputb==-1 and inputc==-1:
        break
   
    w(inputa,inputb,inputc)
    array[0][0][0]=3
    
    print( "w(" +str(inputa)+", " +str(inputb)+ ", " + str(inputc) +") = "+ str(array[inputa][inputb][inputc]))
    

#배열은 만들어둠! 음 어떻게 저장할지 고민해보기
#현재 문제, 다 0으로 들어가고 함수가 한번밖에 호출이 안되고 있음 (재귀 X) -> 재귀적으로 호출이 안되는 것이 가장 큰 문제!
    
