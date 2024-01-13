import sys
from functools import cmp_to_key

input = sys.stdin.readline

N = int(input())
A = sorted([*input().split()], key=cmp_to_key(lambda a, b: int(b + a) - int(a + b)))
print(int("".join(A)))
