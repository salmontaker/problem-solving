import sys
from collections import defaultdict

input = sys.stdin.readline

words = [[*input().strip()] for _ in range(int(input()))]
size_of_words = defaultdict(int)
for word in words:
    for i in range(len(word)):
        size_of_words[word[i]] += 10 ** (len(word) - i - 1)

num = 9
value_of_words = defaultdict(int)
for size in sorted(size_of_words.items(), key=lambda x: -x[1]):
    value_of_words[size[0]] = num
    num -= 1

for i in range(len(words)):
    for j in range(len(words[i])):
        words[i][j] = str(value_of_words[words[i][j]])
    words[i] = "".join(words[i])

print(sum(map(int, words)))
