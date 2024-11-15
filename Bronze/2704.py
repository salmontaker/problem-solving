import sys

input = sys.stdin.readline

for _ in range(int(input())):
    H, M, S = map(lambda x: f"{int(x):06b}", input().split(":"))
    T = ["".join(bits) for bits in zip(H, M, S)]
    print("".join(T), "".join([H, M, S]))
