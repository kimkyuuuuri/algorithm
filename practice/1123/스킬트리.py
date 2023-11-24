
answer = 0
  
    for j in skill_trees:
        index=-1
        flag=0
        for i in skill:
            if i in j:
                temp_index=j.index(i)
                if index>temp_index:
                    flag=1
                    break
                index=temp_index
            else:
                index=len(j)+1
        if flag==0:  
            answer+=1
