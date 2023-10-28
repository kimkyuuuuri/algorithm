import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
n=int(input())
answer=1

# 팩토리얼 재귀로 구현하기
def fac(num):
    global answer
    if num==1 or num==0:
        return answer
    answer*=num
    fac(num-1)

fac(n)
print(answer)


