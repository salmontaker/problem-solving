import sys
from math import factorial
from itertools import permutations

for line in sys.stdin.readlines():
    S, N = line.split()
    N = int(N)

    print(f"{S} {N} = ", end="")
    if factorial(len(S)) < N:
        print("No permutation")
    else:
        for idx, value in enumerate(permutations(S)):
            if idx == N - 1:
                print(*value, sep="")
                break
