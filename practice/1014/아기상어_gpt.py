import sys
from collections import deque

n = int(input().strip())
array = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    array.append(list(map(int, input().split())))

now_size = 2
eat = 0

def bfs(x, y):
    que = deque([(x, y, 0)])  # Include the starting point and its distance
    visited = [[False] * n for _ in range(n)]
    visited[x][y] = True

    answer_list = []

    while que:
        x, y, dist = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = True

                if array[nx][ny] > now_size:
                    continue

                que.append((nx, ny, dist + 1))

                if array[nx][ny] < now_size and array[nx][ny] > 0:
                    answer_list.append((dist + 1, nx, ny))

    if answer_list:
        return sorted(answer_list, key=lambda x: (x[0], x[1], x[2]))
    else:
        return []

answer = 0

for i in range(n):
    for j in range(n):
        if array[i][j] == 9:
            while True:
                answer_list = bfs(i, j)
                if len(answer_list) == 0:
                    break
                temp = answer_list[0]
                i, j = temp[1], temp[2]
                array[i][j] = 0
                eat += 1

                answer += temp[0]
                if eat == now_size:
                    now_size += 1
                    eat = 0
            break

print(answer)
