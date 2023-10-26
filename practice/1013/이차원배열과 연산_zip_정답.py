from collections import Counter
import sys
input=sys.stdin.readline

r, c, k = map(int, input().split())


array=[]
row_n=3
col_n=3
for i in range(3):
    array.append(list(map(int, input().split())))
answer=0
    
while answer <= 100:
    if r <= len(array) and c <= len(array[0]) and array[r - 1][c - 1] == k:
        break
    
    answer+=1
    row_n=len(array)
    col_n=len(array[0])
    
    # 시뮬레이션으로 구현
    if row_n>=col_n:
        max_size=0
        for i in range(row_n):
            count_list=Counter(array[i])
            del count_list[0]
            count_sort_list=sorted(count_list.items(), key=lambda x:(x[1],x[0]))
           
            temp_array=[]
            for j in count_sort_list:
                temp_array.append(j[0])
                temp_array.append(j[1])
            array[i]=temp_array
            max_size=max(max_size, len(temp_array))
        
        for j in range(len(array)):
            if len(array[j]) < max_size:
                array[j] += [0] * (max_size - len(array[j]))

    else:
        temp_list=list(map(list, zip(*array)))
        max_size=0
        for i in range(col_n):
            count_list=Counter(temp_list[i])
            del count_list[0]
            
            count_sort_list=sorted(count_list.items(), key=lambda x:(x[1],x[0]))
            temp_array=[]
            for j in count_sort_list:
                temp_array.append(j[0])
                temp_array.append(j[1])

            temp_list[i]=temp_array
            max_size=max(max_size, len(temp_array))
        for j in range(len(temp_list)):
            if len(temp_list[j]) < max_size:
                temp_list[j] += [0] * (max_size - len(temp_list[j]))
        array=list(map(list, zip(*temp_list)))
       
 
if answer>100:
    answer=-1
print(answer)

