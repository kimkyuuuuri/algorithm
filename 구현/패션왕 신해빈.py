n=int(input())
result=1
for i in range(n):
        dic={}
        count=int(input())
        for j in range(count):
                a,b=input().split()
                if b in dic:
                        dic[b]=dic[b]+1
                else:
                        dic[b]=1
        for k in dic.values():
                result*=(k+1)
                
        result-=1
        print(result)
        result=1
                
        
