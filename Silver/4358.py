import sys
from collections import defaultdict

trees = sys.stdin.readlines()
species = defaultdict(int)
for name in trees:
    species[name.strip()] += 1

for name, count in sorted(species.items()):
    print(f"{name} {count / len(trees) * 100:.4f}")
