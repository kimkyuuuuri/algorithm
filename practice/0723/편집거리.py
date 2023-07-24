a=input()
#행 
b=input()
#열 

d=[[0 for _ in range(len(b)+1)] for j in range(len(a)+1)]

# index는 글자수에 직접 접근하여 확인하기
for i in range(len(b)+1):
    d[0][i]=i
for i in range(len(a)+1):
    d[i][0]=i
    
    
for i in range(1,len(a)+1):
    for j in range(1,len(b)+1):
        if a[i-1]==b[j-1]:
            d[i][j]=d[i-1][j-1]

        else:
            d[i][j]=min(d[i-1][j-1], d[i-1][j], d[i][j-1])+1

print(d[len(a)][len(b)])
        
        
