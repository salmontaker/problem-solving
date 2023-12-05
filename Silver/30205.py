import sys

input = sys.stdin.readline

N, M, P = map(int, input().split())
B = [sorted(map(int, input().split())) for _ in range(N)]
I = 0


def can_win(v):
    global P, I

    for i in range(I + 1):
        if v <= P * 2**i:
            P *= 2**i
            I -= i
            return True

    return False


for b in B:
    for v in b:
        if v == -1:
            I += 1
        elif can_win(v):
            P += v
        else:
            print(0)
            exit(0)

    P *= 2**I
    I = 0

print(1)
