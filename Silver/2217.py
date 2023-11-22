import sys

input = sys.stdin.readline

N = int(input())
R = sorted([int(input()) for _ in range(N)])
A = 0

for i in range(N):
    A = max(A, R[i] * (N - i))

print(A)
