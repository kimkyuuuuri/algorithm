def solution(food_times, k):
    dic = {i:v for i, v in enumerate(food_times)}
    print(dic)
    while dic:
        now=min(dic)
        print(now)
        want=now*len(dic)
        if want<k:
            dic.pop(now)
            k-=want
            for i in range(len(dic)):
                dic[i]-=now
        else:
            break
    print(k)
    index=k%len(food_times)
    
    return food_times[index]
