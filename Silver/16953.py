import sys

input = sys.stdin.readline

A, B = map(int, input().split())
C = 1

while A < B:
    if B % 2 == 0:
        B = B // 2
    elif B % 10 == 1:
        B = B // 10
    else:
        break
    C += 1

print(C if A == B else -1)
