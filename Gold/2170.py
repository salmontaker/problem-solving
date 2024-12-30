import sys

input = sys.stdin.readline

N = int(input())
LINES = sorted([[*map(int, input().split())] for _ in range(N)])
HEAD = TAIL = -sys.maxsize

answer = 0
for head, tail in LINES:
    if TAIL < head:
        answer += TAIL - HEAD
        HEAD = head
    if TAIL < tail:
        TAIL = tail

print(answer + TAIL - HEAD)
