import sys, copy

input = sys.stdin.readline

N = int(input())
A = [0] + [*map(int, input().split())]

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

    print(*B[1:])
