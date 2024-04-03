import sys

input = sys.stdin.readline

N = int(input())
A = [[*map(int, input().split())] for _ in range(N)]
D = [[0] * N for _ in range(N)]
D[0][0] = 1

for y in range(N):
    for x in range(N):
        if A[y][x] != 0 and D[y][x] != 0:
            for dy, dx in [(A[y][x], 0), (0, A[y][x])]:
                Y, X = y + dy, x + dx
                if Y < N and X < N:
                    D[Y][X] += D[y][x]

print(D[N - 1][N - 1])
