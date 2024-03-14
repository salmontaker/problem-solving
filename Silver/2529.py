import sys

input = sys.stdin.readline


def check(depth, num):
    return A[depth - 1] < num if S[depth - 1] == "<" else A[depth - 1] > num


def dfs(depth):
    if depth == N + 1:
        answer.append([*A])
        return

    for i in range(10):
        if not V[i]:
            if depth == 0 or check(depth, i):
                V[i] = 1
                A.append(i)
                dfs(depth + 1)
                A.pop()
                V[i] = 0


N = int(input())
S = input().split()
A = []
V = [0] * 10
answer = []

dfs(0)

print(*answer[-1], sep="")
print(*answer[0], sep="")
