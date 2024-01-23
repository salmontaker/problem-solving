import sys

input = sys.stdin.readline

N = int(input())
D = [i for i in range(N + 1)]

for i in range(2, N + 1):
    j = 1
    while j * j <= i:
        if D[i] > D[i - j * j] + 1:
            D[i] = D[i - j * j] + 1
        j += 1

print(D[N])
