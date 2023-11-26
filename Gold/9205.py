import sys
from collections import deque

input = sys.stdin.readline


def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


for _ in range(int(input())):
    N = int(input())
    pos = [[*map(int, input().split())] for _ in range(N + 2)]
    graph = [[] for _ in range(N + 2)]
    visited = [0] * (N + 2)

    for i in range(N + 2):
        for j in range(N + 2):
            if i != j and distance(pos[i], pos[j]) <= 1000:
                graph[i].append(j)

    queue = deque([0])
    visited[0] = 1
    while queue:
        cur = queue.popleft()
        for next in graph[cur]:
            if not visited[next]:
                queue.append(next)
                visited[next] = 1

    print("happy" if visited[N + 1] else "sad")
