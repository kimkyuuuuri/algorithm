# 하루 전까지 보관 가능 
def change(date):
    date_sum=0
    array = date.split('.')
    date_sum+=int(array[0])*28*12 + int(array[1])*28 + int(array[2])
    return date_sum

def solution(today, terms, privacies):
    # privacies에 있는 날짜 + terms에 해당하는 날짜 > today: 파기
    # terms 딕셔너리로 수정
    terms_dic = {i.split(' ')[0]:int(i.split(' ')[1]) for i in terms }
    answer=[]
    today_sum = change(today)
    for i in range(len(privacies)):
        privacies_array = privacies[i].split(' ')
        date_sum= change(privacies_array[0])
        result_sum= date_sum + terms_dic[privacies_array[1]]*28
        if result_sum <= today_sum:
            answer.append(i+1)
        
        
    return answer
