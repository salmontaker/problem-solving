import sys

input = sys.stdin.readline

N = int(input())
A = [*map(int, input().split())]
D = [0] * N

D[0] = A[0]
for i in range(1, N):
    D[i] = max(A[i], A[i] + D[i - 1])

print(max(D))
