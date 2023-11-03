import sys
from collections import deque

input = sys.stdin.readline


def melt(y, x):
    cnt = 0
    for dy, dx in delta:
        Y, X = y + dy, x + dx
        if -1 < Y < N and -1 < X < M and area[Y][X] == 0:
            cnt += 1

    return max(area[y][x] - cnt, 0)


def bfs(y, x):
    queue = deque([(y, x)])
    visited[y][x] = 1

    while queue:
        y, x = queue.popleft()
        for dy, dx in delta:
            Y, X = y + dy, x + dx
            if -1 < Y < N and -1 < X < M and area[Y][X] != 0 and not visited[Y][X]:
                queue.append((Y, X))
                visited[Y][X] = 1


N, M = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N)]
delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
temp = deque()
year = 0


while True:
    visited = [[0] * M for _ in range(N)]
    cnt = 0

    # 빙산 덩어리 개수
    for y in range(N):
        for x in range(M):
            if area[y][x] != 0 and not visited[y][x]:
                bfs(y, x)
                cnt += 1

    if cnt >= 2:
        print(year)
        break

    elif cnt == 0:
        print(0)
        break

    # 빙산이 녹아내리는 높이 계산
    for y in range(N):
        for x in range(M):
            if area[y][x] != 0:
                temp.append((y, x, melt(y, x)))

    # 배열에 데이터 반영
    while temp:
        y, x, m = temp.popleft()
        area[y][x] = m

    year += 1
