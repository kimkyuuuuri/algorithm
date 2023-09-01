import sys
input= sys.stdin.readline
n= int(input())

for i in range(n):
    m=int(input())
    array=[]
    answer=1
    for i in range(m):
        a,b = map(int, input().split())
        array.append([a,b])
    array.sort()

    # min_rank 갱신
    min_rank=array[0][1]
    for i in range(1,m):
        temp = array[i][1]
        if temp < min_rank:
            min_rank = temp
            answer+=1
                
    print(answer)
   
        
        
        
        
