n=input()
m=input()

while m in n:
    array = n.split(m)
    n=''.join(array)
    
if n is not "":        
    print(n)
else:
    print("FRULA")

# 반복을 줄일 수 잇을까? 
#내생각에는 빼는거는 계속 해야하함. 
# 스택을 쓰면 더 유리할까? 붙여서 전체 비교, 붙여서 전체 비교 이게 너무 비효율적
# 여기서 떠올릴 아이디어 !!! stack [:4] 이런식으로 문자 전체 !!



