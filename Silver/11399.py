import sys

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
p = sorted(list(map(int, input().split())))
print(f"{sum([sum(p[:i+1]) for i in range(n)])}")
