#재귀 함수 호출하는 건데, 배열을 이용해서 한번 구한 내용은 더이상 구하지 않도록 하는 것이 핵심 !
#문제는 어떤 배열을 선언해야하지?
import sys
sys.setrecursionlimit(10**6)

def w(a,b,c):
    global array
    if a<=0 or b<=0 or c<=0: 
        return 1
   
    elif a<b and b<c:
        if array[a][b][c-1]==-1:
            array[a][b][c-1]=w(a,b,c-1)
            
        if array[a][b-1][c-1]==-1:
            array[a][b-1][c-1]=w(a,b-1,c-1)
            
        if array[a][b-1][c]==-1:
            array[a][b-1][c]=w(a,b-1,c)
        
        array[a][b][c]=array[a][b][c-1]+array[a][b-1][c-1]-array[a][b-1][c]
        
        return array[a][b][c]
    
    else:
        if array[a-1][b][c]==-1:
            
            array[a-1][b][c]=w(a-1,b,c)
            
        if array[a-1][b-1][c]==-1:
            array[a-1][b-1][c]=w(a-1,b-1,c)
            
        if array[a-1][b][c-1]==-1:
            array[a-1][b][c-1]=w(a-1,b,c-1)
            
        if array[a-1][b-1][c-1]==-1:
            array[a-1][b-1][c-1]=w(a-1,b-1,c-1)
            
        array[a][b][c]=array[a-1][b][c]+array[a-1][b-1][c]+array[a-1][b][c-1]-array[a-1][b-1][c-1]
     
        return array[a][b][c]

while True:
    inputa,inputb,inputc = map(int,sys.stdin.readline().split())
    
    
    array = [[[-1 for x in range(51)] for j in range(51)] for i in range(51)]
    
    if inputa==-1 and inputb==-1 and inputc==-1:
        break
    elif inputa<=0 or inputb<=0 or inputc<=0:
        print( "w(" +str(inputa)+", " +str(inputb)+ ", " + str(inputc) +") = "+ str(1))
    elif inputa>20 or inputb>20 or inputc>20:
    
        print( "w(" +str(inputa)+", " +str(inputb)+ ", " + str(inputc) +") = "+ str(1048576))
    
          
    else:
     
              
        w(inputa,inputb,inputc)

    
        print( "w(" +str(inputa)+", " +str(inputb)+ ", " + str(inputc) +") = "+ str(array[inputa][inputb][inputc]))
    

#배열은 만들어둠! 음 어떻게 저장할지 고민해보기
