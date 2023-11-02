ans = ""
cnt = 0
for c in list(input()):
    if c == "X":
        cnt += 1
    else:
        if cnt % 2 != 0:
            print(-1)
            exit(0)
        else:
            ans += "AAAA" * (cnt // 4) + "BB" * (cnt % 4 // 2) + "."
            cnt = 0
ans += "AAAA" * (cnt // 4) + "BB" * (cnt % 4 // 2)
print(-1 if cnt % 2 != 0 else ans)
