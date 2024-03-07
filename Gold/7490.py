import sys
from itertools import product

input = sys.stdin.readline

OP = [" ", "+", "-"]
for _ in range(int(input())):
    N = int(input())
    A = [*range(1, N + 1)]
    for p in product(OP, repeat=N - 1):
        formula = "".join([f"{A[0]}"] + [f"{op}{num}" for op, num in zip(p, A[1:])])
        if eval(formula.replace(" ", "")) == 0:
            print(formula)
    print()
