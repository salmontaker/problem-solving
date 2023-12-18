import sys
from collections import deque

input = sys.stdin.readline


def bfs(node):
    queue = deque([node])
    visited = [0] * (N + 1)
    visited[node] = 1
    cnt = 1

    while queue:
        current = queue.popleft()
        for next in graph[current]:
            if not visited[next]:
                queue.append(next)
                visited[next] = 1
                cnt += 1

    return cnt


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)

max_cnt = 0
answer = []

for i in range(1, N + 1):
    cnt = bfs(i)
    if max_cnt < cnt:
        max_cnt = cnt
        answer = [i]
    elif max_cnt == cnt:
        answer.append(i)

print(*sorted(answer))
