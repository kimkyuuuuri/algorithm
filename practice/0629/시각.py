# 시각 -> 하루 24시간
# 12시, 5분, 30초 // 24 * 60 * 60
count=0
n=int(input())
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                count+=1
print(count)

