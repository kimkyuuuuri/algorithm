n=int(input())
m=[]
for i in range(n):
    a,b=input().split()
    m.append((int(a),int(b)))
    
sorted_=sorted(m,key=lambda x: (x[1],x[0]))

last_time=0
count=0
for i in range(n):  
    if int(sorted_[i][0])>=int(last_time):
        last_time=sorted_[i][1]
        count+=1

print(count)
    
