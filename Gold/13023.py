import sys

input = sys.stdin.readline


def dfs(depth, current):
    if depth == 5:
        print(1)
        exit()

    for next in G[current]:
        if not V[next]:
            V[next] = 1
            dfs(depth + 1, next)
            V[next] = 0


N, M = map(int, input().split())
G = [[] for _ in range(N)]
V = [0] * N

for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

for i in range(N):
    dfs(0, i)

print(0)
