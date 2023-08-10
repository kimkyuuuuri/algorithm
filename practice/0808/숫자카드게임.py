n, m = map(int, input().split())
array = []

for i in range(n):
    temp_array = list(map(int, input().split()))
    temp_array.sort()
    array.append(temp_array[0])
array.sort(reverse=True)
print(array[0])


