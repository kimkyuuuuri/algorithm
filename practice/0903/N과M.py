import sys
input = sys.stdin.readline

#1부터 N까지 자연수 중에서 중복없이 M개

n,m=map(int, input().split())
array=[]
def dfs():
    if len(array)==m:
        # ' ' 안에 공백있으면 결과 띄어쓰기 추가됨! 
        print(' '.join(map(str,array)))
        

    for i in range(n):
        if i+1 not in array:
            array.append(i+1)
            dfs()
            array.pop()

dfs()
    
    


    


    
