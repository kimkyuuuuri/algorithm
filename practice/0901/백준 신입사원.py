# 백준 신입사원
import sys
input= sys.stdin.readline

n=int(input())


for i in range(n):
    m=int(input())
    array=[]
    answer=0
    max_value=m+1
    for i in range(m):
        a,b = map(int, input().split())
        array.append([a,b])
    array.sort()
    for i in array:
        if i[1]<max_value:
            max_value=i[1]
            answer+=1

    print(answer)
        
