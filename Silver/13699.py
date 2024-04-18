import sys

input = sys.stdin.readline

N = int(input())
D = [0] * (N + 1)
D[0] = 1

if N > 0:
    D[1] = 1
    for i in range(2, N + 1):
        for j in range(i):
            D[i] += D[j] * D[i - j - 1]

print(D[N])
