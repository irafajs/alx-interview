#!/usr/bin/python3
"""
Shebang to create a py script
"""


def minOperations(n):
    """return n number that op will take to reahc the result"""
    def minOperations(n):
        if n == 1:
            return 0
    list_db = [0] * (n + 1)
    for i in range(2, n + 1):
        list_db[i] = i
        for j in range(2, i):
            if i % j == 0:
                list_db[i] = min(list_db[i], list_db[j] + (i // j))
    return list_db[n]
