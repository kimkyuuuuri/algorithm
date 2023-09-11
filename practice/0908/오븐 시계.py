array = list(map(int, input().split()))
time = array[0] * 60 + array[1]
time += int(input())

new_time = time//60
new_time_2 = time%60

new_time=new_time%24
    
print(new_time, end =' ')
print(new_time_2  )
