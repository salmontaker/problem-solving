n, l, k = map(int, input().split())
problems = [list(map(int, input().split())) + [True] for _ in range(n)]
points = 0

for problem in problems:
    if k == 0:
        break
    elif problem[1] <= l and problem[2]:
        problem[2] = False
        points += 140
        k -= 1

for problem in problems:
    if k == 0:
        break
    elif problem[0] <= l and problem[2]:
        points += 100
        k -= 1

print(points)
