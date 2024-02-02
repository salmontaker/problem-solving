import sys

input = sys.stdin.readline

N, K = map(int, input().split())
S = input().strip()

y, x = 0, 0
for _ in range(min(N, K)):
    for ch in S:
        if ch == "U":
            y -= 1
        elif ch == "D":
            y += 1
        elif ch == "L":
            x -= 1
        elif ch == "R":
            x += 1

        if y == 0 and x == 0:
            print("YES")
            exit()

print("NO")
