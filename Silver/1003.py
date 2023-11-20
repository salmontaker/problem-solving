import sys

input = sys.stdin.readline

N = 40
d0 = [1, 0] + [0] * (N - 1)
d1 = [0, 1] + [0] * (N - 1)

for n in range(2, N + 1):
    d0[n] = d0[n - 1] + d0[n - 2]
    d1[n] = d1[n - 1] + d1[n - 2]

for _ in range(int(input())):
    n = int(input())
    print(d0[n], d1[n])
