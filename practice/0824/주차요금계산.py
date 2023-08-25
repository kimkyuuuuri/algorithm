import math
def solution(fees, records):
    answer = []
    dic = {}
    for i in records:
        temp = i.split(' ')
        time = int(temp[0].split(':')[0])*60 + int(temp[0].split(':')[1])
   
        if temp[2]=="IN":
            if temp[1] not in dic.keys():
                dic[temp[1]]=[[time, 23*60+59]]
            else:
                dic[temp[1]].append([time, 23*60+59])
        else:
            dic[temp[1]][-1][1]=time

    for i in sorted(dic.keys()):
        result=0
        temp=0
        for j in dic[i]:
            temp+=j[1]-j[0]
        result = fees[1] + math.ceil(max(0,temp-fees[0])/fees[2])*fees[3]
        answer.append(result)
 
    return answer
