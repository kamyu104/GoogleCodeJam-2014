# Copyright (c) 2015 kamyu. All rights reserved.
#
# Google Code Jam 2014 World Finals - Problem C. Symmetric Trees
# https://code.google.com/codejam/contest/7214486/dashboard#s=p2
#
# Time:  O(N^3 * logN) = O(N * (sum(klogk)) in the worst case of all vertices on the symmetry line
# Space: O(N^2), for each node a, con[a][b] + con[b][a] = O(N)
#

import sys

def encode_subtree(a, parent):
    children = []
    for b in con[a]:
        if b != parent:
            if con[a][b] == -1:
                con[a][b] = encode_subtree(b, a)
            children.append(con[a][b])

    m = '(' + colors[a]
    for c in sorted(children):
        m += ',' + c
    return m + ')'


def rec_symmetric(a, parent):
    first_pair = {}
    for b in con[a]:
        if b != parent:
            if con[a][b] in first_pair:
                del first_pair[con[a][b]]
            else:
                first_pair[con[a][b]] = b

    keys = list(first_pair.values())
    if len(keys) == 0:
        return True

    ok = rec_symmetric(keys[0], a)
    if len(keys) == 1 or not ok:
        return ok

    # Non-root is only allowed one unpaired branch.
    if len(keys) > 2 or parent != -1:
        return False

    return rec_symmetric(keys[1], a)


def symmetric():
    # No vertex in the middle line.
    for a in xrange(N):
        for b in con[a]:
            if con[a][b] == con[b][a]:
                return True

    # Pick a vertex in the middle line.
    for a in xrange(N):
        if rec_symmetric(a, -1):
            return True

    return False


sys.setrecursionlimit(100000)
for case in xrange(input()):
    colors = []
    con = []

    N = input()
    for i in xrange(N):
        colors.append(raw_input().strip())
        con.append({})

    for i in xrange(N - 1):
        e = map(int, raw_input().strip().split())
        a = e[0] - 1
        b = e[1] - 1
        con[a][b] = -1
        con[b][a] = -1

    for a in xrange(N):
        encode_subtree(a, -1)

    if symmetric():
        print "Case #%d: SYMMETRIC" % (case+1)
    else:
        print "Case #%d: NOT SYMMETRIC" % (case+1)
