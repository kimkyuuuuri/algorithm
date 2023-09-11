dic_x= {}
dic_y= {}
for i in range(3):
    x,y = map(int, input().split())
    if x not in dic_x.keys():
        dic_x[x]=1
    else:
        dic_x[x]+=1

    if y not in dic_y.keys():
        dic_y[y]=1
    else:
        dic_y[y]+=1

for i in  dic_x.keys():
    if dic_x[i]==1:
        print(i,end=' ')

for j in  dic_y.keys():
    if dic_y[j]==1:
        print(j)
