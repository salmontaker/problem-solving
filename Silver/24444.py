import sys
from collections import deque

input = sys.stdin.readline


def bfs(start):
    queue = deque([start])
    visited[start] = 1
    cnt = 1

    while queue:
        next = queue.popleft()
        for node in matrix[next]:
            if not visited[node]:
                queue.append(node)
                visited[node] = cnt + 1
                cnt += 1


N, M, R = map(int, input().split())
matrix = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    matrix[a].append(b)
    matrix[b].append(a)

for i in range(1, N + 1):
    matrix[i].sort()

bfs(R)
for v in visited[1:]:
    print(v)
