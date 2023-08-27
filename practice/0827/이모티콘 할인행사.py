from itertools import product
def solution(users, emoticons):
    answer = []
    result=[]
    discount = [10,20,30,40]
    array = list(product(discount,repeat=len(emoticons)))

    for k in array:
        temp_plus=0
        temp_money=0
        for user in users:
            temp_sum=0
            for emoticon in range(len(emoticons)):
                if k[emoticon] >= user[0]:
                    temp_sum+=int(emoticons[emoticon]*(100-k[emoticon])/100)
            if temp_sum>=user[1]:
                temp_plus+=1
            else:
                temp_money+=temp_sum

        result.append([temp_plus, temp_money])
        result.sort(reverse=True)
    answer=result[0]
    return answer
