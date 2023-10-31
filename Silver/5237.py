def dfs(v):
    visited[v] = 1
    for i in range(N):
        if matrix[v][i] and not visited[i]:
            dfs(i)


for _ in range(int(input())):
    N, K, *C = map(int, input().split())
    matrix = [[0] * N for _ in range(N)]
    visited = [0] * N
    for i in range(0, K * 2, 2):
        a, b = C[i], C[i + 1]
        matrix[a][b] = matrix[b][a] = 1
    dfs(0)
    print("Not connected." if 0 in visited else "Connected.")
