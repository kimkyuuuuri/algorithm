result=0
index=0
while food_times:
    food_times.remove(0)
    food_times[index%len(food_times)]-=1
    index+=1

if len(food_times)>0:
    return index%len(food_times)
else:
    return-1
        
