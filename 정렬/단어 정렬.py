n=int(input())
array=[]
arraylen=[]


for i in range(n):
        array.append(input())

set_list=set(array)
new_array=list(set_list)
new_array.sort()
new_array.sort(key=len)

for i in range(len(new_array)):
        print(new_array[i])



