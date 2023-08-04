def solution(players, callings):
    dic = {value:key for key,value in enumerate(players)}
    for i in callings:
        index = dic[i]
        dic[i]-=1
        dic[players[index-1]]+=1
        players[index], players[index-1] = players[index-1], players[index]
       
    return players
