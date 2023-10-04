import sys

input = sys.stdin.readline
print = sys.stdout.write

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
cnt = 0

for coin in reversed(coins):
    cnt += k // coin
    k %= coin

print(f"{cnt}")
