def solution(picks, minerals):
    
    minerals=minerals[0:sum(picks*5)]
    array=[[0,0,0] for i in range(len(minerals)//5+1)]
    
    for i in range(len(minerals)):
        if minerals[i]=="diamond":
            array[i//5][0]+=1
        elif minerals[i]=="iron":
            array[i//5][1]+=1
        else:
            array[i//5][2]+=1
    
    array.sort(reverse=True, key=lambda x:(x[0],x[1],x[2]))
    index=0
    result=0
    for i in range(len(picks)):
        for j in range(picks[i]):
            if index>=len(array):
                break
            if i==0:
                result+=array[index][0]+array[index][1]+array[index][2]
            elif i==1:
                result+=array[index][0]*5+array[index][1]+array[index][2]
            elif i==2:
                result+=array[index][0]*25+array[index][1]*5+array[index][2]
            index+=1
       
    return result
