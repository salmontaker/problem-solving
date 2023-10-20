import sys

p = sys.stdout.write
n = int(input())
for i in range(n):
    p(" " * (n - i - 1) + "*" * (2 * i + 1) + "\n")
for i in reversed(range(n - 1)):
    p(" " * (n - i - 1) + "*" * (2 * i + 1) + "\n")
