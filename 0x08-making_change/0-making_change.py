#!/usr/bin/python3
"""
Sheabng to create a PY script
"""


def makeChange(coins, total):
    """calcule fewes number of coins to reach total"""

    coins.sort(reverse=True)

    min_coins = float('inf')
    stack = [(0, total, 0)]

    while stack:
        index, remaining_total, count = stack.pop()

        if remaining_total == 0:
            min_coins = min(min_coins, count)
            continue

        if remaining_total < 0 or count >= min_coins:
            continue

        for i in range(index, len(coins)):
            stack.append((i, remaining_total - coins[i], count + 1))

    return min_coins if min_coins != float('inf') else -1
