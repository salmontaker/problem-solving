from itertools import combinations

for p in combinations(sorted([int(input()) for _ in range(9)]), 7):
    if sum(p) == 100:
        for _ in p:
            print(_)
        break
