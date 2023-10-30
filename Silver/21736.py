from collections import deque


def bfs(y, x):
    queue = deque([(y, x)])
    cnt = 0
    while queue:
        y, x = queue.popleft()
        if grid[y][x] == "P":
            cnt += 1

        for dy, dx in dir:
            Y, X = y + dy, x + dx
            if -1 < Y < N and -1 < X < M and grid[Y][X] != "X" and not visited[Y][X]:
                queue.append((Y, X))
                visited[Y][X] = True

    return cnt


N, M = map(int, input().split())
grid = [list(input()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
answer = 0

for y in range(N):
    for x in range(M):
        if grid[y][x] == "I":
            answer = bfs(y, x)
            break

print(answer if answer else "TT")
