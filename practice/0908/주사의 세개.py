from collections import Counter

array = list(map(int, input().split()))
counter_array = Counter(array)

length= len(counter_array)
answer=0
if length == 3:
    answer=max(counter_array.keys())*100

elif length ==2:
    answer=0
    for i in counter_array.keys():
        if counter_array[i]==2:
            answer+=1000+i*100
else:
    answer=array[0]*1000 + 10000
    
print(answer)
