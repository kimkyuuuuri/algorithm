#직접 작성한 초기 코드
array=[7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)-1):
    min_num=array[i]
    num=array[i+1]
    index=i+1
    for j in range(len(array)):
        
        if(j<i):
            continue
        
        if num>array[j]:
            index=j
            num=array[j]
        
    if min_num>num:
        array[index]=min_num
        array[i]=num
    
print(array)

#답안
for i in range(len(array)):
	min_index=i
    for j in range(i+1,len(array)):
    	if array[min_index]>array[j]:
        	min_index=j
    array[i], array[min_index]=array[min_index],aray[i] #스와프 코드

print(array)
