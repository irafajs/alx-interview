#!/usr/bin/python3
"""
Shebang to create a py script
"""


def island_perimeter(grid):
    """search and return the ilsand perimeter"""
    lon = len(grid)
    lar = len(grid[0])

    def dfs(w, h):
        """search for the island"""
        if w < 0 or w >= lon or h < 0 or h >= lar or grid[w][h] == 0:
            return 1
        if grid[w][h] == 1:
            grid[w][h] = 2
            return dfs(w - 1, h) + dfs(w - 1, h) + dfs(
                    w, h + 1) + dfs(w, h - 1)
        return 0

    perimeter = 0
    for h in range(lon):
        for w in range(lar):
            if grid[h][w] == 1:
                perimeter += dfs(h, w)
    return perimeter
