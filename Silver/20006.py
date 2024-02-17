import sys

input = sys.stdin.readline


def join_room(L, N):
    for room in ROOMS:
        if abs(room[0][0] - L) <= 10 and len(room) < M:
            room.append((L, N))
            return

    ROOMS.append([(L, N)])


P, M = map(int, input().split())
ROOMS = []
for _ in range(P):
    L, N = input().split()
    join_room(int(L), N)

for room in ROOMS:
    print("Started!" if len(room) == M else "Waiting!")
    for player in sorted(room, key=lambda x: x[1]):
        print(*player)
