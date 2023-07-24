array = [[0 for _ in range(8)] for j in range(8)]
x=[2, -2, 2, -2, 1, -1, 1, -1]
y=[1, 1, -1, -1, 2, 2, -2, -2]

count=0
n=input()
print(n[0])
col = ord(n[0])-96
row = int(n[1])
for i in range(8):
    
    ncol=col+x[i]
    nrow=row+y[i]
    if (nrow>0 and nrow<=8) and (ncol>0 and ncol<=8):
        count+=1
  
print(count)
