import sys
from collections import Counter

I = sys.stdin.readline
N, M = map(int, I().split())
C = Counter([i for _ in range(N) if len(i := I()) > M])
A = sorted(C)
A = sorted(A, key=len, reverse=True)
A = sorted(A, key=C.get, reverse=True)
sys.stdout.write("".join(A))
