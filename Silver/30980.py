import sys

input = sys.stdin.readline

N, M = map(int, input().split())
A = [[*input().strip()] for _ in range(N * 3)]

for row in range(0, N * 3, 3):
    target = A[row + 1 :][0]

    for col in range(0, M * 8, 8):
        formula = target[col : col + 8]
        answer = int(formula[1]) + int(formula[3])
        check = int("".join(formula[5:7]).rstrip("."))
        offset = int(check > 9)

        if answer == check:
            A[row + 1][col] = "*"
            A[row + 1][col + 6 + offset] = "*"
            for k in range(1, 6 + offset):
                A[row][col + k] = "*"
                A[row + 2][col + k] = "*"
        else:
            A[row][col + 3] = "/"
            A[row + 1][col + 2] = "/"
            A[row + 2][col + 1] = "/"

for a in A:
    print(*a, sep="")
