import sys

input = sys.stdin.readline

N = int(input())
A = [[*map(int, input().split())] for _ in range(N)]
D = [[0] * 3 for _ in range(N)]

for i in range(3):
    D[0][i] = A[0][i]

for i in range(1, N):
    D[i][0] = A[i][0] + min(D[i - 1][1], D[i - 1][2])
    D[i][1] = A[i][1] + min(D[i - 1][0], D[i - 1][2])
    D[i][2] = A[i][2] + min(D[i - 1][0], D[i - 1][1])

print(min(D[N - 1]))
