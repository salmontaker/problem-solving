import sys

input = sys.stdin.readline

N, M = map(int, input().split())
y, x, d = map(int, input().split())

# 북, 동, 남, 서
delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
room = [input().split() for _ in range(N)]
ans = 0


# 1: 전방, -1: 후방
def check(dir):
    dy, dx = delta[d]
    return room[y + dy * dir][x + dx * dir]


def move(dir):
    global y, x

    dy, dx = delta[d]
    y = y + dy * dir
    x = x + dx * dir


while True:
    # 현재 칸 청소
    if room[y][x] == "0":
        room[y][x] = "2"
        ans += 1

    # 청소되지 않은 빈 칸 검사
    cnt = 0
    for dy, dx in delta:
        ny, nx = y + dy, x + dx
        if room[ny][nx] == "0":
            cnt += 1

    if cnt == 0:
        if check(-1) != "1":
            move(-1)
        else:
            break
    else:
        # 반시계 방향으로 회전
        d = (d + 3) % 4

        # 앞쪽 칸이 청소되지 않은 빈 칸인 경우, 한 칸 전진
        if check(1) == "0":
            move(1)

print(ans)
