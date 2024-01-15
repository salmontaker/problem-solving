import sys
from functools import cmp_to_key

input = sys.stdin.readline

K, N = map(int, input().split())
A = [input().strip() for _ in range(K)]
MAX = str(max(map(int, A)))

for _ in range(N - K):
    A.append(MAX)

answer = sorted(A, key=cmp_to_key(lambda a, b: int(b + a) - int(a + b)))
print("".join(answer))
