#!/usr/bin/python3
"""
Shebang to create a py script
"""


def canUnlockAll(boxes):
    """method to check and unlock the box if the
       have a key, return true, else return false"""

    n = len(boxes)
    if (n == 0):
        return ('No box to visit')
    visited = [False] * n
    visited[0] = True

    def dfs(box_index):
        """method to search thorough each box"""
        visited[box_index] = True
        for key in boxes[box_index]:
            if not visited[key]:
                dfs(key)

    dfs(0)

    return all(visited)
