import sys
from itertools import combinations

input = sys.stdin.readline


def accuracy_of(model):
    correct = 0
    for answer, predict in zip(A, model):
        if answer == predict:
            correct += 1

    return correct / M


def ensemble(comb):
    result = []
    for models in comb:
        temp = []
        for i in range(M):
            cnt = [0, 0]
            for model in models:
                cnt[model[i]] += 1

            temp.append(0 if cnt[0] > cnt[1] else 1)

        result.append(temp)

    return result


N, M = map(int, input().split())
A = [*map(int, input().split())]
B = [[*map(int, input().split())] for _ in range(N)]

highest = max(map(accuracy_of, B))
for select in range(3, N + 1, 2):
    models = ensemble([*combinations(B, select)])
    for model in models:
        if highest < accuracy_of(model):
            print(1)
            exit()

print(0)
