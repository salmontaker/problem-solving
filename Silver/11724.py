import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline


def dfs(v):
    visited[v] = True
    for i in range(1, N + 1):
        if matrix[v][i] and not visited[i]:
            dfs(i)


N, M = map(int, input().split())
matrix = [[False] * (N + 1) for _ in range(N + 1)]
visited = [False] * (N + 1)
answer = 0

for _ in range(M):
    a, b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = True

for i in range(1, N + 1):
    if not visited[i]:
        dfs(i)
        answer += 1

print(answer)
