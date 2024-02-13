import sys

input = sys.stdin.readline


def dfs(y):
    global answer

    if y == N:
        answer += 1
        return

    for x in range(N):
        if V1[x] or V2[y + x] or V3[y - x + N - 1]:
            continue

        V1[x] = V2[y + x] = V3[y - x + N - 1] = 1
        dfs(y + 1)
        V1[x] = V2[y + x] = V3[y - x + N - 1] = 0


N = int(input())
V1 = [0] * N
V2 = [0] * (2 * N + 1)
V3 = [0] * (2 * N + 1)

answer = 0
dfs(0)
print(answer)
