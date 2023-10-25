e, s, m = map(int, input().split())
ans = 1
while True:
    if (ans - e) % 15 == 0 and (ans - s) % 28 == 0 and (ans - m) % 19 == 0:
        print(ans)
        break
    ans += 1
