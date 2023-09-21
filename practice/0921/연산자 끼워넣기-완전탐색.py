# 완전탐색으로 구현
# 연산자 곱하기, 나누기를 순열으로 랜덤으로 뽑아내서
# 순서는 더하기 빼기 곱하기 나누기
from itertools import permutations
import sys
input=sys.stdin.readline
n=int(input())
numbers=list(map(int, input().split()))
func=list(map(int, input().split()))
func_array=[]
for  i in range(len(func)):
    for j in range(func[i]):
        func_array.append(i)

        
result_array=[]

# 2111 이렇게 되어있는것을 
for i in permutations(func_array):
    # i가 list!
    result=0
    result=numbers[0]
    for j in range(len(i)):
  
        
        if i[j]==0:
            result=result+numbers[j+1]
        elif i[j]==1:
            result=result-numbers[j+1]
        elif i[j]==2:
            result=result*numbers[j+1]
        else:
            if result <0:
                temp=-result
                temp//=numbers[j+1]
                result=-temp
            else:
                result//=numbers[j+1]
    result_array.append(result)
                
        
result_array.sort()
print(result_array[-1])
print(result_array[0])
   # result=0
   # for j in numbers:


   
        
    
