n=input()
alpha_str=[]
num=0
for i in n:
    if i.isalpha():
        alpha_str.append(i)
    else:
        num+=int(i)

alpha_str.sort()
result=''.join(alpha_str)+str(num)
print(result)
