import sys

input = sys.stdin.readline
print = sys.stdout.write

input()
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())), reverse=True)

answer = sum(map(lambda x, y: x * y, a, b))
print(f"{answer}")
