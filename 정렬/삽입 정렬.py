array=[7,5,9,0,3,1,6,2,4,8]
for i in range(1,len(array)):
    for j in range(i,0,-1):
        if array[j] < array[j-1]:
            # 정렬이 되어있는 상태이기 때문에 바로 앞과 비교하면됨.
            array[j],array[j-1]=array[j-1],array[j]
        else:
            break
print(array)
