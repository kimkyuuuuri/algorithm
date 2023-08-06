n=input()
length = len(n)//2
left=0
right=0

for i in range(length):
    left+=int(n[i])
    right+=int(n[len(n)-1-i])

if left==right:
    print("LUCKY")
else:
    print("READY")
