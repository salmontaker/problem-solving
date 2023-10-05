import sys

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
distances = list(map(int, input().split()))
payments = list(map(int, input().split()))
min_payment = payments[0]

costs = 0

for i in range(n - 1):
    if min_payment > payments[i]:
        min_payment = payments[i]

    costs += min_payment * distances[i]

print(f"{costs}")
