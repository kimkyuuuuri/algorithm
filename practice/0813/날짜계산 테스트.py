def to_days(date):
    year, month, day = map(int, date.split('.'))
    return year*28*12 + month*28 + day


privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
terms = ["A 6", "B 12", "C 3"]

# terms는 dictionary로 저장 !
months = {v[0]: int(v[2:]) * 28 for v in terms}
print(months['C'])


# privacies는 마지막 알파벳으로 terms에서 찾아서 더해야됨.
result = []
for i in privacies:
    
    
