from collections import deque


def bfs(y, x):
    queue = deque([(y, x)])
    while queue:
        y, x = queue.popleft()

        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            Y, X = y + dy, x + dx
            if Y > -1 and Y < N and X > -1 and X < M and ground[Y][X] == 1:
                queue.append((Y, X))
                ground[Y][X] = 0


for _ in range(int(input())):
    M, N, K = map(int, input().split())

    ground = [[0] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        ground[y][x] = 1

    cnt = 0
    for y in range(N):
        for x in range(M):
            if ground[y][x] == 1:
                bfs(y, x)
                cnt += 1

    print(cnt)
