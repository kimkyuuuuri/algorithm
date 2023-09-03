import sys
input = sys.stdin.readline

n=int(input())
array=[]
dic={}
for i in range(n):
    temp=input().rstrip()
    index=1
    for j in range(len(temp)-1,-1,-1):
        if temp[j] in dic.keys():
            dic[temp[j]]+=index
        else:
            dic[temp[j]]=index
        index*=10
        
value_list = list(dic.values())
value_list.sort(reverse=True)
start=9
answer=0

for i in value_list:
    answer+=i*start
    start-=1
print(answer)
    
    


    


    
