import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
IN = deque([input().strip() for _ in range(N)])
OUT = deque([input().strip() for _ in range(N)])
answer = 0

while IN:
    if IN[0] != OUT[0]:
        IN.remove(OUT.popleft())
        answer += 1
    else:
        IN.popleft()
        OUT.popleft()

print(answer)
