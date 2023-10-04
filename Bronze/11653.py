import sys

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
div = 2

while n != 1:
    if n % div == 0:
        print(f"{div}\n")
        n /= div
    else:
        div += 1
