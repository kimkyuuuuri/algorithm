import sys
from itertools  import permutations
from collections import Counter
input = sys.stdin.readline

# 배열 count로 알파벳 수 세기
n=int(input())
array=[]
num_array=[9,8,7,6,5,4,3,2,1,0]
arrays=[]
answer=0
result_array=[]
#index로 사용 
for i in range(n):
    temp=input().rstrip()
    array+=temp
    arrays.append(temp)


set_array=set(array)
dic = { i:v for v,i in enumerate(set_array)}

#알파벳에 숫자 할당 
for i in permutations(num_array[0:len(set_array)], len(set_array)):
    temp_answer=0
    for j in arrays:
        temp=''
        for k in j:
            temp+=str(i[dic[k]])
        
        temp_answer+=int(temp)
    answer=max(answer,temp_answer )
print(answer)
            
        
    


    
