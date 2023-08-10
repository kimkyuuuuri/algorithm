n=input()
x=ord(n[0])-97
y=int(n[1])-1

dx=[2,2,-2,-2,1,1,-1,-1]
dy=[1,-1,1,-1,2,-2,2,-2]
answer=0

for i in range(8):
    nx=x+dx[i]
    ny=y+dy[i]
    if nx <8 and ny<8 and nx>-1 and ny>-1:
        answer+=1
        
print(answer)
