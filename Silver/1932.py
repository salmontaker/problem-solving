import sys

input = sys.stdin.readline

N = int(input())
A = [[*map(int, input().split())] + [-1] * (N - i - 1) for i in range(N)]
D = [[0] * N for _ in range(N)]
D[0][0] = A[0][0]

for i in range(N - 1):
    for j in range(i + 1):
        D[i + 1][j] = max(D[i + 1][j], D[i][j] + A[i + 1][j])
        D[i + 1][j + 1] = max(D[i + 1][j + 1], D[i][j] + A[i + 1][j + 1])

print(max(D[N - 1]))
