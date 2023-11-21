def solution(arrayA, arrayB):
    
    if len(arrayA) == 1:
        if arrayA[0] == arrayB[0]:
            return 0
        else:
            return max(arrayA[0], arrayB[0])
    
    gcd1=gcd(arrayA[0],arrayA[1])
    for i in range(2, len(arrayA)):
        gcd1=gcd(gcd1, arrayA[i])
    for i in arrayB:
        if i % gcd1==0:
            gcd1=0
            break
            
    gcd2=gcd(arrayB[0],arrayB[1])
    for i in range(2, len(arrayB)):
        gcd2=gcd(gcd2, arrayB[i])
    
    for i in arrayA:
        if i % gcd2==0:
            gcd2=0
            break
            
    answer= max(gcd1, gcd2)
    return answer

def gcd(a,b):
    if b==0:
        return a
    else:
        if a<b:
            return gcd(a,b%a)
        else:
            return gcd(b,a%b)
        
    
