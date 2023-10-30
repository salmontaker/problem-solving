from collections import deque


def bfs(y, x, color, visited, blind):
    queue = deque([(y, x)])
    visited[y][x] = True
    while queue:
        y, x = queue.popleft()
        for dy, dx in dir:
            Y, X = y + dy, x + dx
            if -1 < Y < N and -1 < X < N and not visited[Y][X]:
                if blind and color != "B" and PAINT[Y][X] in ["R", "G"]:
                    queue.append((Y, X))
                    visited[Y][X] = True
                elif PAINT[Y][X] == color:
                    queue.append((Y, X))
                    visited[Y][X] = True


N = int(input())
PAINT = [list(input()) for _ in range(N)]
visited_a = [[False] * N for _ in range(N)]
visited_b = [[False] * N for _ in range(N)]
dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
a, b = 0, 0

for y in range(N):
    for x in range(N):
        if not visited_a[y][x]:
            bfs(y, x, PAINT[y][x], visited_a, False)
            a += 1
        if not visited_b[y][x]:
            bfs(y, x, PAINT[y][x], visited_b, True)
            b += 1

print(a, b)
