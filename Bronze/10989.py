import sys

input = sys.stdin.readline
print = sys.stdout.write

data = [0] * 10001

for _ in range(int(input())):
    data[int(input())] += 1

for idx, value in enumerate(data):
    for _ in range(value):
        print(f"{idx}\n")
