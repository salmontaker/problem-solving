import sys
from collections import deque

input = sys.stdin.readline
print = sys.stdout.write

for _ in range(int(input())):
    prompts = input()
    n = int(input())
    arr = input().strip("[]\n")
    arr = deque(map(int, arr.split(","))) if arr else []

    reverse = False
    err = False

    for p in prompts:
        if p == "R":
            reverse = not reverse
        elif p == "D":
            if arr:
                if reverse:
                    arr.pop()
                else:
                    arr.popleft()
            else:
                err = True
                break

    if reverse:
        arr.reverse()

    if err:
        print("error\n")
    else:
        print(f"{list(arr)}\n".replace(" ", ""))
