n=int(input())

def factorial(a):
    if a!=0:
        return factorial(a-1)*a
    return 1;

print(factorial(n))
    
