import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
Q = deque([N])
X = [-1] * (10**5 + 1)
X[N] = 0

while Q:
    cur = Q.popleft()
    for next in [cur + 1, cur - 1, cur * 2]:
        if -1 < next < len(X) and X[next] == -1:
            Q.append(next)
            X[next] = X[cur] + 1

print(X[K])
