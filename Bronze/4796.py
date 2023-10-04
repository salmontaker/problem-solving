import sys

input = sys.stdin.readline
print = sys.stdout.write

cnt = 1

while True:
    l, p, v = map(int, input().split())

    if l == 0 and p == 0 and v == 0:
        break
    else:
        print(f"Case {cnt}: {v // p * l + (v % p if v % p < l else l)}\n")
        cnt += 1


# 20일짜리 휴가에 8일중 5일동안만 사용 가능한 경우 : 14일
# 01 02 03 04 05 06 07 08 09 10
# O  O  O  O  O  X  X  X  O  O
# 11 12 13 14 15 16 17 18 19 20
# O  O  O  X  X  X  O  O  O  O
