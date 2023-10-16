a, b, c, m = map(int, input().split())
hp, answer = 0, 0

for _ in range(24):
    if hp + a > m:
        hp -= c
        if hp < 0:
            hp = 0
    else:
        hp += a
        answer += b

print(answer)
