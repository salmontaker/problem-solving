import sys

input = sys.stdin.readline
print = sys.stdout.write

n, m = map(int, input().split())
ans = list({input() for _ in range(n)} & {input() for _ in range(m)})

print(f"{len(ans)}\n")
for _ in sorted(ans):
    print(f"{_}")
