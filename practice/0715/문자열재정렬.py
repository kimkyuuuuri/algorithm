n=input()
result_str=[]
r_str=''
result_num=0
for i in n:
    if i.isalpha():
        result_str.append(i)
    elif i.isdigit():
        result_num+=int(i)
result_str.sort()
r_str=''.join(result_str)
print(r_str+str(result_num))
    
