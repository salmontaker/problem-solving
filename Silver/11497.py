import sys

input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    A = sorted([*map(int, input().split())])
    B = [*A[0:N:2], *reversed(A[1:N:2])]
    print(max([abs(B[i] - B[(i + 1) % N]) for i in range(N)]))
