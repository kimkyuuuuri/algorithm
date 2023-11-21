def solution(k, tangerine):
    dic={}
    answer=0
    for i in tangerine:
        if i not in dic.keys():
            dic[i]=1
        else:
            dic[i]+=1
    
    new_dic=sorted(dic.items(), key=lambda x:x[1], reverse=True)
    for i in new_dic:
        answer+=1
        k-=i[1]
        if k<=0:
            break
    return answer



