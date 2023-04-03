n=int(input())
count=0
dic={}
dic2={}
listt=[]
input_list=list(map(int,input().split()))

dic[0]=input_list[0]
# 예외 - 이미 중간에 끼니까 reset이 되어야한다! 
for i in range(0,n):
        for j in range(0,i):
                dic[j]=dic[j]+input_list[i]
                if dic[j]==0 :
                        dic2[j]='T'
                        listt.append(j)
                        
                
                        
                        
        dic[i]=input_list[i]
        print(dic)
print(dic2)
print(len(dic2))
