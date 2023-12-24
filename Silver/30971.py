import sys
from itertools import permutations

input = sys.stdin.readline

N, K = map(int, input().split())
A = [*map(int, input().split())]
B = [*map(int, input().split())]
C = [*map(int, input().split())]

answer = -1
for p in permutations([(A[i], B[i], C[i]) for i in range(N)]):
    temp = 0
    for i in range(1, N):
        if p[i - 1][2] * p[i][2] <= K:
            temp += p[i - 1][0] * p[i][1]
        else:
            temp = -1
            break

    answer = max(answer, temp)

print(answer)
