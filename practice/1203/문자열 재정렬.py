# 문자를 오름차순으로 정렬 먼저
array = input()
# 문자열, 숫자 따로 분리
char_array=[]
num_array=[]

for i in array:
    if i.isdigit():
        num_array.append(int(i))
    elif i.isalpha():
        char_array.append(i)


char_array.sort()
num=sum(num_array)

print(''.join(char_array),end='')
print(str(num))


