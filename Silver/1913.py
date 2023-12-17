import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
K = N // 2

A = [[0] * N for _ in range(N)]
A[K][K] = 1
Y, X = K, K


def f(dy, dx, n):
    global Y, X

    Y, X = Y + dy, X + dx
    A[Y][X] = n + 1


for i in range(K):
    for j in range(2 * i + 1):
        f(-1, 0, A[Y][X])
    for j in range(2 * i + 1):
        f(0, 1, A[Y][X])
    for j in range(2 * i + 2):
        f(1, 0, A[Y][X])
    for j in range(2 * i + 2):
        f(0, -1, A[Y][X])

for i in range(N - 1):
    f(-1, 0, A[Y][X])

for a in A:
    print(*a)

for y in range(N):
    for x in range(N):
        if A[y][x] == M:
            print(y + 1, x + 1)
            exit()
