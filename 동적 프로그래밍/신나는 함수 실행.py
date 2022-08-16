#재귀 함수 호출하는 건데, 배열을 이용해서 한번 구한 내용은 더이상 구하지 않도록 하는 것이 핵심 !
#문제는 어떤 배열을 선언해야하지?

def w(a,b,c):
    if a<=0 or b<=0 or c<=0:
        return 1
    elif a>20 or b>20 or c>20:
        return w(a,b,c)
    elif a<b and b<c:
        return w(a,b,c-1)+ w(a,b-1,c-1) -w(a,b-1,c)
    else:
        return w(a-1,b,c) + w(a-1,b-1,c) + w(a-1,b,c-1) -w(a-1,b-1,c-1)

while True:
    inputa,inputb,inputc = map(int,input().split())
    arraya=[0]*inputa
    arrayb=[0]*inputb
    arrayc=[0]*inputc
    
    if inputa==-1 and inputb==-1 and inputc==-1:
        break

    print( "w(" +str(inputa)+", " +str(inputb)+ ", " + str(inputc) +") = "+ str(w(inputa,inputb,inputc)))

#배열은 만들어둠! 음 어떻게 저장할지 고민해보기
