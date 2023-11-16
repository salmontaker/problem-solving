import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
A = [0] + [*map(int, input().split())]
dist = [-1] * (N + 1)
start, end = map(int, input().split())

Q = deque([start])
dist[start] = 0

while Q:
    # 현재 위치
    current = Q.popleft()
    # 점프할 수 있는 거리는 현재 위치의 배수임.
    for multiply in range(1, N // A[current] + 1):
        # 좌우로 이동 가능함
        for delta in [-1, 1]:
            # 따라서 다음 위치는 현재 위치의 배수 + 현재 위치
            next = A[current] * multiply * delta + current
            # 범위를 넘지 않고 방문한 적이 없을경우 방문
            if 0 < next < N + 1 and dist[next] == -1:
                Q.append(next)
                dist[next] = dist[current] + 1

print(dist[end])
