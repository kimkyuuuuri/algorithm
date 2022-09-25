num=int(input())

def count(n):
    array=[]
    array.append('0')
    for i in range(n):
        array.append("l")

    for i in range(1,n+1):
        for j in range(i,n+1):
            if j%i==0:
                if array[j]=="u":
                    array[j]="l"
                else:
                    array[j]="u"
    print(array.count("u"))

for i in range(num):
    a=int(input())
    count(a)
    
