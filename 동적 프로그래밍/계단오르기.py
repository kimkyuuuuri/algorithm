n = int(input())

d = [0]*(n+1)
d[1]=0
d[2]=1
d[3]=1
d[4]=1
if (n>3):
    for i in range(4,n+1):
    
        d[i]=d[i-2]+d[i-3]
        
print(d[n]%796796)
