a,b =map(int,input().split())
#해결, 2부터 i 제곱근까지 검사하면 된다
#for문 안에 범위설정할 수 있다.
# isPrime함수에서 2부터 i의 제곱근까지 검사하면 된다고 함..고민해보

def isPrime(num):
    number=2
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            number+=1
            return False

    return True

for i in range(a,b+1):
    
    if isPrime(a):
        print(a)
    a+=1
        
