import sys
input=sys.stdin.readline
n=int(input())
set_array=set()

for i in range(n):
    a,b = input().split()
    if b=="enter":
        set_array.add(a)
    elif b=="leave":
        set_array.remove(a)
        
answer_list=sorted(list(set_array),reverse=True)
for i in answer_list:
    print(i)
