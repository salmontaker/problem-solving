import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
grid = [[*input().split()] for _ in range(N)]
houses = []
chickens = []
for y in range(N):
    for x in range(N):
        if grid[y][x] == "1":
            houses.append((y, x))
        if grid[y][x] == "2":
            chickens.append((y, x))

answer = 10**6
for combo in combinations(chickens, M):
    temp = 0
    for house in houses:
        dist = 10**6
        for chicken in combo:
            dist = min(dist, abs(house[0] - chicken[0]) + abs(house[1] - chicken[1]))
        temp += dist
    answer = min(answer, temp)

print(answer)
