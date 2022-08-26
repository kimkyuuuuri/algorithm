import heapq
n=int(input())

heap=[]

#최대힙 이용해서 배열을 정렬하고, 0이 들어오면 가장 큰 값 출력하면 됨
#그러면 배열에서 가장 큰 값을 가장 앞에 두자

for i in range(n):
    num=int(input())
    
    if num==0:
        if len(heap)==0:
            print(0)
        else:
            print(-(heapq.heappop(heap)))
    else:
        heapq.heappush(heap,-num)

