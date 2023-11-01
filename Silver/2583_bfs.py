from collections import deque


def bfs(y, x):
    queue = deque([(y, x)])
    rect[y][x] = 0
    area = 1

    while queue:
        y, x = queue.popleft()
        for dy, dx in d:
            Y, X = y + dy, x + dx
            if -1 < Y < M and -1 < X < N and rect[Y][X]:
                queue.append((Y, X))
                rect[Y][X] = 0
                area += 1

    return area


M, N, K = map(int, input().split())
rect = [[1] * N for _ in range(M)]
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
areas = []

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            rect[y][x] = 0


for y in range(M):
    for x in range(N):
        if rect[y][x]:
            areas.append(bfs(y, x))

print(len(areas))
print(*sorted(areas))
