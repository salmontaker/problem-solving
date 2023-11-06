import sys

input = sys.stdin.readline


def dfs(n):
    visited[n] = 1
    for i in range(1, N + 1):
        if connected[n][i] and not visited[i]:
            dfs(i)


N, M = map(int, input().split())
connected = [[0] * (N + 1) for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    connected[a][b] = connected[b][a] = 1

dfs(1)
cows = [str(i) for i in range(2, N + 1) if not visited[i]]
print("\n".join(cows) if cows else 0)
