def to_days(date):
    year, month, day = map(int, date.split('.'))
    return year*28*12 + month*28 + day

def solution(today, terms, privacies):
    answer = []
    today_date = to_days(today)
    months = {v[0]: int(v[2:]) * 28 for v in terms}
    
    for i in range(len(privacies)):
        temp = to_days(privacies[i].split(' ')[0]) + months[privacies[i].split(' ')[1]]
        if temp-1 < today_date:
            answer.append(i+1)
            
    answer.sort()
    return answer
