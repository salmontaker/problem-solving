import sys

input = sys.stdin.readline
N, M, R = map(int, input().split())
A = [input().split() for _ in range(N)]

for _ in range(R):
    for d in range(min(N, M) // 2):
        y_max = N - d - 1
        x_max = M - d - 1
        temp = A[d][d]

        for x in range(d, x_max):
            A[d][x] = A[d][x + 1]
        for y in range(d, y_max):
            A[y][x_max] = A[y + 1][x_max]
        for x in range(x_max, d, -1):
            A[y_max][x] = A[y_max][x - 1]
        for y in range(y_max, d, -1):
            A[y][d] = A[y - 1][d]

        A[d + 1][d] = temp

for a in A:
    print(*a)
