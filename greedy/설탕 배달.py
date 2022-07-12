n=int(input())
count=0
k=n
five= k//5
k=k%5
three=k//3
k=k%3


while True:
    
    if k==0:
        print(five+three)
        break

    elif five<=0:
        if k%3==0:
            three+=k//3
            print(three)
            break
        else:
            print(-1)
            break
    
        
    else :
        
        five-=1
        k=k+5
       
        three+=k//3
        k=k%3
        
        
        

        
        
    


