import sys

input = sys.stdin.readline

books = [int(input()) for _ in range(int(input()))]
next = len(books)
answer = 0
for cur in reversed(books):
    if cur == next:
        next -= 1
    else:
        answer += 1

print(answer)
