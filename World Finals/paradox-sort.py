# Copyright (c) 2015 kamyu. All rights reserved.
#
# Google Code Jam 2014 World Finals - Problem D. Paradox Sort
# https://code.google.com/codejam/contest/7214486/dashboard#s=p3
#
# Time:  O(N^2 * N!)
# Space: O(N)
#

def dfs(i, removed, visited):
    visited.add(i)
    for j in xrange(len(prefer[i])):
        if prefer[i][j] == 'Y':
            if j not in visited and j not in removed:
                dfs(j, removed, visited)


def valid(partial):
    B = partial[0]
    for i in partial:
        if prefer[i][B] == 'Y':
            B = i

    removed = set(partial)
    removed.remove(B)

    # Trivial case.
    if A in removed: return False

    # Case (i)
    if A == B:
        for i in xrange(N):
            if i != A and i not in removed:
                if prefer[A][i] != 'Y':
                    return False
        return True

    # Case (ii)
    visited = set([B])
    dfs(A, removed, visited)
    for i in xrange(len(prefer[B])):
        if prefer[B][i] == 'Y':
            visited.add(i)
    return len(visited.union(removed)) == N


def paradox_sort():
    visited = set()
    dfs(A, set(), visited)
    if len(visited) != N:
        return "IMPOSSIBLE"

    partial = []
    for i in xrange(N):
        for j in xrange(N):
            if j not in partial and valid(partial + [j]):
                partial += [j]
                break
    return ' '.join(map(str, partial))


for case in xrange(input()):
    [N, A] = map(int, raw_input().strip().split())
    prefer = []
    for i in xrange(N):
        prefer.append(raw_input().strip())
    print "Case #%d: %s" % (case+1, paradox_sort())
