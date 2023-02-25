# 파이썬에서 리스트는 배열 기능을 포함하고, 내부적으로 연결리스트 자료구조를 채택해서 append(), remove() 메소드를 지원한다.
# 대괄호안에 원소를 넣고, 쉼표로 구분한다.

a = [1,2,3,4,5]
print(a)

# 인덱스는 0부터 시작한다.
print(a[0])
print(a[2])

# 빈 리스트 선언: list() 혹은 대괄호
a = list()
print(a)

a = []
print(a)

# 문제에서 크기가 N인 1차원 리스트를 초기화해야한다면
n = 10
a = [0]*n
print(a)

# 인덱싱과 슬라이싱: 양수와 음수 모두 사용
a = [1,2,3,4,5]
print(a[-1])
print(a[-3])

a[3]=7
print(a)

# 범위로 가져오기
# a[시작 인덱스:끝 인덱스 -1]이 출력된다. (4번째 인덱스까지 출력하고 싶으면 5를 입)
print(a[1:5])

# 리스트 컴프리헨션
# 초기화하는 방법으로 대괄호 안에 조건문과 반복문을 넣는 방식으로 리스트를 초기화할 수 있다.
# 코딩 테스트에서 2차원 리스트를 초기화할 때 효과적이다. (반드시 이 방식을 사용하자)
array = [i for i in range(20) if i % 2 == 1]
print(array)

array = [j*j for j in range(5) if j % 2 == 0]
print(array)

n=3
m=4

# 반복을 위해서 변수를 사용해야하지만 의미가 없을 때 _ 를 사용한다.
array = [[0] * m for _ in range(n)]
print(array)

# 리스트와 관련된 기타 메서드
a=[1,4,3]


# 오른쪽에 삽입 - 시간 복잡도 O(1)
a.append(2)
print(a)

# 오름차순 정렬 - 시간 복잡도 O(NlogN)
a.sort()
print(a)

# 내림차순 정렬 - 시간 복잡도 O(NlogN)
a.sort(reverse = True)
print(a)

# 리스트 원소 뒤집기 - 시간 복잡도 O(N)
a.reverse()
print(a)

# 특정 인덱스에 데이터 추가 (0,1,2 자리에 추가) - 시간 복잡도 O(N)
a.insert(2,10)
print(a)

# 특정 값인 데이터 개수 세기 - 시간 복잡도 O(N)
print(a.count(10))
a.insert(0,2)
print(a)
print(a.count(2))
 
# 특정 값 데이터 삭제 - 시간 복잡도 O(N)
a.remove(2)
print(a)
a.remove(2)
print(a)

## 주의
# append 함수와 다르게 insert함수는 원소의 개수가 n일때 시간 복잡도는 O(N)이다. 시간 초과를 주의하자. (remove 함수도 동일)

# 특정 원소를 모두 삭제하고 싶다면?
# 포함된 원소를 모두 확인해서 그 원소가 remove_set네 포함되지 않았을 때만 새로운 리스트에 추가하자.

a = [1,2,3,4,5,5,5]
print(a)
remove_set = [3,5]

result = [i for i in a if i not in remove_set]
print(result)



