paper = [[0] * 101 for _ in range(101)]
answer = 0

for _ in range(int(input())):
    a, b = map(int, input().split())
    for y in range(b, b + 10):
        for x in range(a, a + 10):
            paper[y][x] = 1

for line in paper:
    answer += sum(line)

print(answer)
