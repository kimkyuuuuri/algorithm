n=input()
answer=0

for i in range(1, len(n)):
    if n[i]!=n[i-1]:
        answer+=1
    

if answer%2!=0:
    answer+=1


print(answer//2)
