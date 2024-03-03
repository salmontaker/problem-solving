import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())
L = len(str(N))

if L < 7:
    for h, w in permutations(range(1, 10), 2):
        for e, l, o, r, d in permutations({*range(10)} - {h, w}, 5):
            A = int(f"{h}{e}{l}{l}{o}")
            B = int(f"{w}{o}{r}{l}{d}")
            if A + B == N:
                print(f"  {A}")
                print(f"+ {B}")
                print("-------")
                print((" " if L == 6 else "  ") + f"{N}")
                exit()

print("No Answer")
