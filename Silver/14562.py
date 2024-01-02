import sys
from collections import deque

input = sys.stdin.readline

for _ in range(int(input())):
    S, T = map(int, input().split())
    Q = deque([(S, T, 0)])
    while Q:
        s, t, cnt = Q.popleft()
        if s == t:
            print(cnt)
            break
        if s * 2 <= t + 3:
            Q.append((s * 2, t + 3, cnt + 1))
        if s + 1 <= t:
            Q.append((s + 1, t, cnt + 1))
