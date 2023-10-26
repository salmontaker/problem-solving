n = int(input())
room = [input() for _ in range(n)]
h, v = 0, 0

for y in range(n):
    cnt = 0
    for x in range(n):
        if room[y][x] == ".":
            cnt += 1
        elif room[y][x] == "X":
            if cnt >= 2:
                h += 1
            cnt = 0
    if cnt >= 2:
        h += 1

for x in range(n):
    cnt = 0
    for y in range(n):
        if room[y][x] == ".":
            cnt += 1
        elif room[y][x] == "X":
            if cnt >= 2:
                v += 1
            cnt = 0
    if cnt >= 2:
        v += 1

print(h, v)
