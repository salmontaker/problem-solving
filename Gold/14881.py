import sys
from math import gcd

input = sys.stdin.readline

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print("NO" if (a < c and b < c) or (c % gcd(a, b) != 0) else "YES")
