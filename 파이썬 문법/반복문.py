import numpy as np

arr_1 = np.arange(100)

li = list()
for i in arr_1:
    li.append(i**2)
print(li)

li_1 = [i**2 for i in arr_1]
print(li)

#반복문 안에 조건문
arr_2 = np.arange(1,11)
li=list()
for i in arr_2:
    if i%2 == 0:
        li.append(i**2)
    else:
        pass

list2 = [i**2 for i in arr_2 if i%2 == 0]
print("list2 테스트")
print(list2)
    
# else 사용
list3 = [i**2 if i%2 == 0 else i for i in arr_2]
print(list3)



        
    
