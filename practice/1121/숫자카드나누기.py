def solution(arrayA, arrayB):
    
    if len(arrayA)==1:
        if arrayA[0] ==arrayB[0]:
            return 0
        else:
            return max(arrayA[0],arrayB[0])
        
    gcda=gcd(arrayA[0],arrayA[1])
    for i in range(2,len(arrayA)):
        gcda=gcd(gcda, arrayA[i])
    for j in arrayB:
        if  j%gcda==0:
            gcda=0
            break
    

    gcdb=gcd(arrayB[0],arrayB[1])
    for i in range(2,len(arrayB)):
        gcdb=gcd(gcdb, arrayB[i])
    for j in arrayA:
        if j%gcdb==0:
            gcdb=0
            break
    
    return max(gcda, gcdb)

# 유클리드 호제법
def gcd(a,b):
    if b==0:
        return a
    else:
        if a>b:
            return gcd(b, a%b)
        else:
            return gcd(a, b%a)
        
    
