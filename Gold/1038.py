import sys
from itertools import combinations

input = sys.stdin.readline

A = []
for i in range(1, 11):
    for num in reversed([*combinations([*reversed(range(10))], i)]):
        A.append(num)

N = int(input())
if N >= len(A):
    print(-1)
else:
    print(*A[N], sep="")
