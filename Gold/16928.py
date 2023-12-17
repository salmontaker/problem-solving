import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
distance = [-1] * 101
ladder = [0] * 101
for _ in range(N + M):
    a, b = map(int, input().split())
    ladder[a] = b

queue = deque([1])
distance[1] = 0
while queue:
    current = queue.popleft()
    if current == 100:
        print(distance[current])
        break

    for delta in range(1, 7):
        next = current + delta
        if next < 101:
            if ladder[next]:
                next = ladder[next]

            if distance[next] == -1:
                queue.append(next)
                distance[next] = distance[current] + 1
