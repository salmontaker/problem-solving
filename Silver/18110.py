import sys

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())

if n == 0:
    print("0")
else:
    offset = int(n * 0.15 + 0.5)
    levels = sorted([int(input()) for _ in range(n)])
    print(f"{int(sum(levels[offset : n - offset]) / (n - offset * 2) + 0.5)}")
