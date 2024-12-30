import sys
from heapq import *

input = sys.stdin.readline


def dijkstra(start):
    heap = [(0, start)]
    DISTANCE[start] = 0

    while heap:
        dist, current = heappop(heap)
        if dist > DISTANCE[current]:
            continue

        for next, weight in GRAPH[current]:
            new_dist = dist + weight
            if new_dist < DISTANCE[next]:
                heappush(heap, (new_dist, next))
                DISTANCE[next] = new_dist


INF = sys.maxsize
V, E = map(int, input().split())
K = int(input())
GRAPH = [[] for _ in range(V + 1)]
DISTANCE = [INF] * (V + 1)

for _ in range(E):
    u, v, w = map(int, input().split())
    GRAPH[u].append((v, w))

dijkstra(K)

for i in range(1, V + 1):
    print(DISTANCE[i] if DISTANCE[i] != INF else "INF")
