import sys

input = sys.stdin.readline

N, M, R = map(int, input().split())
GRAPH = [[] for _ in range(N + 1)]
VISITED = [0] * (N + 1)
ORDER = 1

# 인접 행렬 사용 시 메모리 초과하므로, 인접 리스트 사용해야 함
for _ in range(M):
    a, b = map(int, input().split())
    GRAPH[a].append(b)
    GRAPH[b].append(a)

for i in range(N):
    GRAPH[i].sort()

STACK = [R]
while STACK:
    node = STACK.pop()
    if not VISITED[node]:
        VISITED[node] = ORDER
        ORDER += 1

    # 스택 사용시 먼저 방문할 정점을 나중에 넣어야 함
    for next in reversed(GRAPH[node]):
        if not VISITED[next]:
            STACK.append(next)

print(*VISITED[1:], sep="\n")
