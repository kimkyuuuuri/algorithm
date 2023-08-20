import sys
sys.setrecursionlimit(10**6)
n=int(input())
row=1+(n-1)*4
array = [[0]*row for i in range(row)]

# 안에서 밖으로! 
def recur(num,start, end ,array):
    if num==1:
        array[start][start]=1
        return 
    # start, end 지정
    for i in range(start,end):
        array[start][i]=1
    for i in range(start,end):
        array[i][start]=1
    for i in range(start,end):
        array[end-1][i]=1
    for i in range(start,end):
        array[i][end-1]=1

    n_start=start+2
    n_end=end-2
    n_num=num-1
    recur(n_num,n_start,n_end,array)
        
    
recur(n,0,row,array)
for i in range(row):
    for j in range(row):
        if array[i][j]==0:
            print(' ',end='')
        else:
            print('*',end='')
    print('')
