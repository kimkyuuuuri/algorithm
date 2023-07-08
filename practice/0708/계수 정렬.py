array = [7,5,9,0,3,1,6,2, 9, 1, 4, 8, 0, 5, 2 ]
result_array = [0]*(max(array)+1)



for i in array:
    result_array[i] = result_array[i]+1

for i in range(len(result_array)):
    for j in range(result_array[i]):
        print(i, end=' ')

