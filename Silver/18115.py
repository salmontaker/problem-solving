import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
A = [*map(int, input().split())]
Q = deque()

for n, x in zip(range(1, N + 1), reversed(A)):
    if x == 1:
        Q.appendleft(n)
    elif x == 2:
        Q.insert(1, n)
    elif x == 3:
        Q.append(n)

print(*Q)
