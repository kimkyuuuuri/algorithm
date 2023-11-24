


    answer = 0
    array=[]
    for i in range(1,6):
        for j in list(map(''.join, product(['A','E','I','O','U'],repeat=i))):
            array.append(j)
    
    array.sort()
    answer=array.index(word)+1
    return answer

    
