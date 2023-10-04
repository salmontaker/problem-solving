import sys

input = sys.stdin.readline
print = sys.stdout.write

t = int(input())

if t % 10 == 0:
    print(f"{t // 300} {t % 300 // 60} {t % 300 % 60 // 10}")
else:
    print("-1")
