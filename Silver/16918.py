import sys

input = sys.stdin.readline

R, C, N = map(int, input().split())
A = [[-1] * (C) for _ in range(R)]

for y in range(R):
    for x, value in enumerate([*input().strip()]):
        if value == "O":
            A[y][x] = 0

# 0초와 1초사이에는 아무일도 일어나지 않음.
T = 2

while N >= T:
    for y in range(R):
        for x in range(C):
            # 짝수 시간대에만 폭탄을 설치함.
            if T % 2 == 0:
                if A[y][x] == -1:
                    A[y][x] = T
            elif T - A[y][x] == 3:
                for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    Y, X = y + dy, x + dx
                    if -1 < Y < R and -1 < X < C and A[y][x] != A[Y][X]:
                        A[Y][X] = -1
                A[y][x] = -1

    T += 1

for row in A:
    print(*map(lambda x: "O" if x > -1 else ".", row), sep="")
