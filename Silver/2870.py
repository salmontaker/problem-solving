import sys

input = sys.stdin.readline

answer = []
for _ in range(int(input())):
    buffer = []
    for ch in input().strip():
        if ch.isnumeric():
            buffer.append(ch)
        elif buffer:
            answer.append("".join(buffer))
            buffer = []
    if buffer:
        answer.append("".join(buffer))
        buffer = []

for n in sorted(map(int, answer)):
    print(n)
