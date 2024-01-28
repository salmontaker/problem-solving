import sys

input = sys.stdin.readline

N = int(input())
A = [0] + [int(input()) for _ in range(N)]
D = [0] * (N + 1)

if N < 3:
    print(sum(A))
else:
    for i in range(1, 4):
        D[i] = A[i]
    for i in range(4, N + 1):
        D[i] = min(D[i - 2], D[i - 3]) + A[i]

    print(sum(A) - min(D[N - 1], D[N - 2]))
