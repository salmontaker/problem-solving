import sys
from math import log2

input = sys.stdin.readline

N = int(input())
C = [0] * 64
answer = 0

for n in [*map(int, input().split())]:
    if n != 0:
        C[int(log2(n))] += 1

for i in range(64):
    if C[i] != 0:
        C[i + 1] += C[i] // 2
        C[i] = C[i] % 2
        answer = 2**i

print(answer)
