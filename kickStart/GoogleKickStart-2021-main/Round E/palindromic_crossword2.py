# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Kick Start 2021 Round E - Problem C. Palindromic Crossword
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000043585c/0000000000859dcd
#
# Time:  O(N * M)
# Space: O(N * M)
#
# dfs solution
#

from collections import defaultdict

def get_coordinate(i, j, transposed):
    return (i, j) if not transposed else (j, i)

def get_grid(grid, i, j, transposed):
    return grid[i][j] if not transposed else grid[j][i]

def build_adj(grid, transposed, adj):
    n, m = (len(grid), len(grid[0])) if not transposed else (len(grid[0]), len(grid))
    for i in xrange(n):
        prev = -1
        for j in xrange(m+1):
            if j != m and get_grid(grid, i, j, transposed) != '#':
                continue
            left, right = prev+1, j-1
            while left < right:
                adj[get_coordinate(i, left, transposed)].append(get_coordinate(i, right, transposed))
                adj[get_coordinate(i, right, transposed)].append(get_coordinate(i, left, transposed))
                left, right = left+1, right-1
            prev = j

def iter_dfs(GRID, adj, i, j, lookup):
    result = 0
    if (i, j) in lookup:
        return result
    lookup.add((i, j))
    stk = [(i, j)]
    while stk:
        i, j = stk.pop()
        for ni, nj in reversed(adj[(i, j)]):
            if (ni, nj) in lookup:
                continue
            lookup.add((ni, nj))
            stk.append((ni, nj))
            if GRID[ni][nj] != '.':
                continue
            GRID[ni][nj] = GRID[i][j]
            result += 1
    return result

def palindromic_crossword():
    N, M = map(int, raw_input().strip().split())
    GRID = [list(raw_input().strip()) for _ in xrange(N)]

    adj = defaultdict(list)
    for transposed in xrange(2):
        build_adj(GRID, transposed, adj)
    lookup = set()
    result = 0
    for i in xrange(N):
        for j in xrange(M):
            if GRID[i][j] != '.' and GRID[i][j] != '#':
                result += iter_dfs(GRID, adj, i, j, lookup)
    return "%s\n%s" % (result, "\n".join(("".join(row) for row in GRID)))

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, palindromic_crossword())
