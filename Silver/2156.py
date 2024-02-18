import sys

input = sys.stdin.readline

N = int(input())
A = [0] + [int(input()) for _ in range(N)]
D = [0] * (N + 1)

D[1] = A[1]
if N > 1:
    D[2] = D[1] + A[2]
    for i in range(3, N + 1):
        D[i] = max(D[i - 1], D[i - 2] + A[i], D[i - 3] + A[i - 1] + A[i])

print(D[N])
