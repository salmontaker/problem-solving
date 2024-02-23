import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input())
S = "9876543210"
A = [*reversed(S)]
for i in range(2, 11):
    for c in reversed([*combinations(S, i)]):
        A.append("".join(c))

print(A[N - 1] if N - 1 < len(A) else -1)
