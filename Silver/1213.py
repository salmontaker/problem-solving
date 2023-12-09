cnt = [0] * 26
for ch in input():
    cnt[ord(ch) - ord("A")] += 1

head = ""
mid = ""
for i in range(26):
    if cnt[i] % 2 != 0:
        mid += chr(ord("A") + i)
    head += chr(ord("A") + i) * (cnt[i] // 2)

if len(mid) > 1:
    print("I'm Sorry Hansoo")
else:
    print(head + mid + head[::-1])
