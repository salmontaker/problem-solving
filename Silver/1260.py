from collections import deque


def dfs(start):
    print(start, end=" ")
    visited_dfs[start] = True

    for i in range(1, N + 1):
        if matrix[start][i] and not visited_dfs[i]:
            dfs(i)


def bfs(start):
    queue = deque([start])
    visited_bfs[start] = True

    while queue:
        q = queue.popleft()
        print(q, end=" ")
        for i in range(1, N + 1):
            if matrix[q][i] and not visited_bfs[i]:
                queue.append(i)
                visited_bfs[i] = True


N, M, V = map(int, input().split())
matrix = [[False] * (N + 1) for _ in range(N + 1)]
visited_dfs = [False] * (N + 1)
visited_bfs = [False] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = True

dfs(V)
print()
bfs(V)
