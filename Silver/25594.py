import sys

input = sys.stdin.readline

code = {
    "aespa": "a",
    "baekjoon": "b",
    "cau": "c",
    "debug": "d",
    "edge": "e",
    "firefox": "f",
    "golang": "g",
    "haegang": "h",
    "iu": "i",
    "java": "j",
    "kotlin": "k",
    "lol": "l",
    "mips": "m",
    "null": "n",
    "os": "o",
    "python": "p",
    "query": "q",
    "roka": "r",
    "solvedac": "s",
    "tod": "t",
    "unix": "u",
    "virus": "v",
    "whale": "w",
    "xcode": "x",
    "yahoo": "y",
    "zebra": "z",
}

S = input().strip()
answer = []
offset = 0

for i in range(len(S)):
    if i - offset > 8:
        break

    if S[offset : i + 1] in code:
        answer.append(S[offset])
        offset = i + 1

if offset == len(S):
    print("It's HG!")
    print("".join(answer))
else:
    print("ERROR!")
