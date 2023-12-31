import sys

input = sys.stdin.readline


def swap_and_count(y, x):
    cnt = 0
    for dy, dx in [(1, 0), (0, 1)]:
        Y, X = y + dy, x + dx
        if -1 < Y < N and -1 < X < N:
            A[Y][X], A[y][x] = A[y][x], A[Y][X]
            cnt = max(cnt, count())
            A[Y][X], A[y][x] = A[y][x], A[Y][X]

    return cnt


def count():
    max_cnt = 0

    for i in range(N):
        cur_cnt = 1
        for j in range(1, N):
            if A[i][j] == A[i][j - 1]:
                cur_cnt += 1
            else:
                cur_cnt = 1

            max_cnt = max(max_cnt, cur_cnt)

    for i in range(N):
        cur_cnt = 1
        for j in range(1, N):
            if A[j][i] == A[j - 1][i]:
                cur_cnt += 1
            else:
                cur_cnt = 1

            max_cnt = max(max_cnt, cur_cnt)

    return max_cnt


N = int(input())
A = [[*input().strip()] for _ in range(N)]
answer = 0
for y in range(N):
    for x in range(N):
        answer = max(answer, swap_and_count(y, x))

print(answer)
