import sys
from itertools import combinations
from bisect import bisect

input = sys.stdin.readline

N, M, R = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

width = sorted({abs(x - y) / 2 for x, y in combinations(A, 2)})
ans = 0

for height in B:
    i = bisect(width, R / height)
    if i == 0:
        continue

    ans = max(ans, width[i - 1] * height)

print(f"{ans:.1f}" if ans else -1)
