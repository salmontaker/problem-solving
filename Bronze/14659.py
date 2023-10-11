n = int(input())
height = list(map(int, input().split()))
cnt = 0
max_cnt = 0
max_height = 0

for i in range(n):
    if max_height < height[i]:
        cnt = 0
        max_height = height[i]
    else:
        cnt += 1
        if max_cnt < cnt:
            max_cnt = cnt

print(max_cnt)
