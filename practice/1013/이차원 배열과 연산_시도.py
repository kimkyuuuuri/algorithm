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
    
for _ in range(100):
    answer+=1
    if array[r][c]==k:
        break

    # 시뮬레이션으로 구현
    if row_n>=col_n:
        max_size=0
        for i in range(row_n):
            count_list=Counter(array[i])
            
            count_sort_list=sorted(count_list.items(), key=lambda x:(x[1],x[0]))
           
            temp_array=[]
            for j in count_sort_list:
                temp_array.append(j[0])
                temp_array.append(j[1])
            array[i]=temp_array
            max_size=max(max_size, len(temp_array))
        col_n=max_size
        for j in array:
            if len(j)!=max_size:
                for k in range(max_size-len(j)):
                    j.append(0)
        print(array)

    # 열을 기준으로 !
    else:
        max_size=0
        for i in range(col_n):
            temp_col_array=[]
            for j in range(row_n):
                temp_col_array.append(array[j][i])
                
            count_list=Counter(temp_col_array)
            count_sort_list=sorted(count_list.items(), key=lambda x:(x[1],x[0]))
           
            temp_array=[]
            for j in count_sort_list:
                temp_array.append(j[0])
                temp_array.append(j[1])
            print("temp_array")
            print(temp_array)
            temp_index
            for k in range(row_n):
                array[k][i]=temp_array[k]
                temp_index=k
            
            
            max_size=max(max_size, len(temp_array))
        row_n=max_size
        print("hehre")
        print(array)

     
        print(array)

            

            
            
    
            
                
            
    

   

print(answer)

