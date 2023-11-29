import sys, copy

input = sys.stdin.readline


def f(x):
    return sum(i * x[i] for i in range(1, N + 1))


N = int(input())
A = [0] + [*map(int, input().split())]

cur = f(A)

for _ in range(int(input())):
    L, R = map(int, input().split())
    B = copy.deepcopy(A)

    pos = []
    num = []
    for i in range(1, N + 1):
        if L <= B[i] <= R:
            pos.append(i)
            num.append(B[i])

    num = sorted(num)
    for i in range(R - L + 1):
        B[pos[i]] = num[i]

    if cur < f(B):
        print(*B[1:])
    else:
        print(*A[1:])
