import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline


def is_safe():
    for y, x in TEACHER:
        if find_student(y, x):
            return False

    return True


def find_student(y, x):
    Q = deque([(y, x, d) for d in range(4)])

    while Q:
        y, x, d = Q.popleft()
        Y, X = y + DIR[d][0], x + DIR[d][1]
        if -1 < Y < N and -1 < X < N:
            if ROOM[Y][X] == "S":
                return True
            elif ROOM[Y][X] == "X":
                Q.append((Y, X, d))

    return False


N = int(input())
ROOM = [input().split() for _ in range(N)]
DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]
TEACHER = []
EMPTY = []

for y in range(N):
    for x in range(N):
        if ROOM[y][x] == "T":
            TEACHER.append((y, x))
        elif ROOM[y][x] == "X":
            EMPTY.append((y, x))

for walls in combinations(EMPTY, 3):
    for y, x in walls:
        ROOM[y][x] = "O"

    if is_safe():
        print("YES")
        exit()

    for y, x in walls:
        ROOM[y][x] = "X"

print("NO")
