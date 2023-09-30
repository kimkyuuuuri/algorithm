import sys


n=input()
key=input()
index=0
key_array = []
key_array_last=[]

# key 만들기
alphabets = ["A","B","C","D","E","F","G","H","I","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

for i in key:
    if i not in key_array:
        key_array.append(i)
        
index=0
while True:
    if alphabets[index] not in key_array:
        key_array.append(alphabets[index])
    if len(key_array)==25:
        break
    index+=1
    
for i in range(5):
    key_array_last.append(key_array[i*5:i*5+5])
    
## 문자열 두개씩 나누기 
# 두개씩 pass 하면서

index=0
temp=[]
n_array=[]
while index<len(n):
    
    now = n[index]
    if temp and temp[0]==now:
        if temp[0]=='X':
            temp.append('Q')
        else:
            temp.append('X')
    else:
        temp.append(now)
        index+=1

    if len(temp)==2:
        n_array.append(temp)
        temp=[]
        
if temp:
    temp.append('X')
    n_array.append(temp)

# 표와 문자 로직 합치기
# 어떤 행에 있는지 파악?
answer=''

for temp in n_array:
    # 각 각 행 열 위치찾ㄱ기
    temp1_xy=[]
    temp2_xy=[]
    
    for i in range(5):
        for j in range(5):
            if key_array_last[i][j]==temp[0]:
                temp1_xy.append(i)
                temp1_xy.append(j)
            elif key_array_last[i][j]==temp[1]:
                temp2_xy.append(i)
                temp2_xy.append(j)

    #행이 같을 때
   
    
    if temp1_xy[0]==temp2_xy[0]:
            # 열을 한칸 씩 옮긴다.
        temp[0]=key_array_last[temp1_xy[0]][(temp1_xy[1]+1)%5]
        temp[1]=key_array_last[temp2_xy[0]][(temp2_xy[1]+1)%5]

        # 열이 같을 때
    elif temp1_xy[1]==temp2_xy[1]:
        temp[0]=key_array_last[(temp1_xy[0]+1)%5][temp1_xy[1]]
        temp[1]=key_array_last[(temp2_xy[0]+1)%5][temp2_xy[1]]

    else:
            # 열 교환
        t1=temp1_xy[1]
        t2=temp2_xy[1]
        temp[0]=key_array_last[temp1_xy[0]][t2]
        temp[1]=key_array_last[temp2_xy[0]][t1]
        
    answer+=''.join(temp)
print(answer)
        

