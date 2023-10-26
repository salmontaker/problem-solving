def dfs(y, x, cnt):
    graph[y][x] = "0"

    for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        Y, X = y + dy, x + dx
        if Y > -1 and Y < N and X > -1 and X < N and graph[Y][X] == "1":
            cnt = dfs(Y, X, cnt + 1)

    return cnt


N = int(input())
graph = [list(input()) for _ in range(N)]
answer = []

for y in range(N):
    for x in range(N):
        if graph[y][x] == "1":
            answer.append(dfs(y, x, 1))

print(len(answer))
for c in sorted(answer):
    print(c)
