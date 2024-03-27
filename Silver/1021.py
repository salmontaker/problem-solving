import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
Q = deque(range(1, N + 1))
answer = 0

for target in [*map(int, input().split())]:
    while target != Q[0]:
        if Q.index(target) > len(Q) // 2:
            Q.appendleft(Q.pop())
            answer += 1
        else:
            Q.append(Q.popleft())
            answer += 1
    Q.popleft()

print(answer)
