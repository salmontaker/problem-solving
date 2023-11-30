import sys

input = sys.stdin.readline

N = int(input())
A = [*map(int, input().split())]
D = [1] * N

for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            D[i] = max(D[i], D[j] + 1)

print(max(D))
