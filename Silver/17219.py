import sys

input = sys.stdin.readline
print = sys.stdout.write

n, m = map(int, input().split())
db = dict()

for _ in range(n):
    line = input().split()
    db[line[0]] = line[1]

for _ in range(m):
    print(f"{db[input().rstrip()]}\n")
