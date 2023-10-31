from collections import deque


def bfs(y, x):
    queue = deque([(y, x)])
    area[y][x] = "X"
    while queue:
        y, x = queue.popleft()
        for dy, dx in dir:
            Y, X = y + dy, x + dx
            if -1 < Y < R and -1 < X < C and area[Y][X] == "#":
                queue.append((Y, X))
                area[Y][X] = "X"


R, C = map(int, input().split())
area = [list(input()) for _ in range(R)]
dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
answer = 0
for y in range(R):
    for x in range(C):
        if area[y][x] == "#":
            bfs(y, x)
            answer += 1

print(answer)
