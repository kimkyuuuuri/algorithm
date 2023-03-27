input_num= map(int(),input().split())
while True:
    target = (n//k)*k # 나누어떠러지는 수가 될 때까지 1씩 뺀다.....
    resut += (n-target)
    n = target

    if n < k :
        break

    rusult += 1
    n // = k

    result += (n-1)
    print(result)
