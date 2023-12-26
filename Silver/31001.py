import sys
from collections import defaultdict

input = sys.stdin.readline


def buy(name, amount):
    global M

    price = companies[name] * amount

    if M >= price:
        M -= price
        stocks[name] += amount


def sell(name, amount):
    global M

    delta = stocks[name] if stocks[name] <= amount else amount

    if stocks[name] != 0:
        M += companies[name] * delta
        stocks[name] -= delta


def delta_company(name, delta):
    companies[name] += delta


def delta_group(id, delta):
    for name in groups[id]:
        companies[name] += delta


def delta_group_percent(id, delta):
    for name in groups[id]:
        companies[name] += companies[name] * (delta * 0.01)
        companies[name] = int(companies[name] * 0.1) * 10


def show_balance():
    print(M)


def show_interest():
    interest = 0
    for name, amount in stocks.items():
        interest += companies[name] * amount

    print(M + interest)


N, M, Q = map(int, input().split())
stocks = defaultdict(int)
groups = defaultdict(list)
companies = defaultdict(int)
menu = [
    buy,
    sell,
    delta_company,
    delta_group,
    delta_group_percent,
    show_balance,
    show_interest,
]

for _ in range(N):
    G, H, P = input().split()
    groups[G].append(H)
    companies[H] = int(P)

for _ in range(Q):
    args = input().split()
    if len(args) > 1:
        menu[int(args[0]) - 1](args[1], int(args[2]))
    else:
        menu[int(args[0]) - 1]()
