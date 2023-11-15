import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().split())
board = [input().strip() for _ in range(R)]
delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
# -1: 방문하지 않음, 0: 시작지점, 1 ~ : 이동시간
d1 = [[-1] * C for _ in range(R)]  # 불의 이동시간
d2 = [[-1] * C for _ in range(R)]  # 지훈의 이동시간
q1 = deque()
q2 = deque()

for y in range(R):
    for x in range(C):
        if board[y][x] == "F":
            q1.append((y, x))
            d1[y][x] = 0
        elif board[y][x] == "J":
            q2.append((y, x))
            d2[y][x] = 0


while q1:
    y, x = q1.popleft()
    for dy, dx in delta:
        Y, X = y + dy, x + dx
        if -1 < Y < R and -1 < X < C:
            if d1[Y][X] == -1 and board[Y][X] != "#":
                q1.append((Y, X))
                d1[Y][X] = d1[y][x] + 1

while q2:
    y, x = q2.popleft()
    for dy, dx in delta:
        Y, X = y + dy, x + dx
        if -1 < Y < R and -1 < X < C:
            if d2[Y][X] == -1 and board[Y][X] != "#":
                # 불이 퍼진적 없거나, 지훈의 이동시간이 불의 이동시간보다 작을경우
                if d1[Y][X] == -1 or d1[Y][X] > d2[y][x] + 1:
                    q2.append((Y, X))
                    d2[Y][X] = d2[y][x] + 1
        # 범위를 벗어났다면 탈출에 성공한 것
        else:
            print(d2[y][x] + 1)
            exit(0)

print("IMPOSSIBLE")
