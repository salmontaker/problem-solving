from collections import deque

M, N = map(int, input().split())
grid = [input().split() for _ in range(N)]
dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# 익지 않은 토마토의 수
cnt = 0

# 익은 토마토의 위치
pos = []

# 토마토가 익을 때까지의 최소 날짜
answer = -1


for y in range(N):
    for x in range(M):
        if grid[y][x] == "0":
            cnt += 1
        if grid[y][x] == "1":
            pos.append((y, x))


while pos:
    queue = deque(pos)
    pos = []
    while queue:
        y, x = queue.popleft()
        for dy, dx in dir:
            Y, X = y + dy, x + dx
            if -1 < Y < N and -1 < X < M and grid[Y][X] == "0":
                grid[Y][X] = "1"
                cnt -= 1
                pos.append((Y, X))
    answer += 1

print(answer if cnt == 0 else -1)
