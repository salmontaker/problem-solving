import sys

input = sys.stdin.readline


def dfs(depth, result):
    if depth == N:
        answer[0] = max(answer[0], result)
        answer[1] = min(answer[1], result)
        return

    if B[0]:
        B[0] -= 1
        dfs(depth + 1, result + A[depth])
        B[0] += 1
    if B[1]:
        B[1] -= 1
        dfs(depth + 1, result - A[depth])
        B[1] += 1
    if B[2]:
        B[2] -= 1
        dfs(depth + 1, result * A[depth])
        B[2] += 1
    if B[3]:
        B[3] -= 1
        dfs(depth + 1, int(result / A[depth]))
        B[3] += 1


N = int(input())
A = [*map(int, input().split())]
B = [*map(int, input().split())]

answer = [-(10**9), 10**9]
dfs(1, A[0])
print(*answer, sep="\n")
