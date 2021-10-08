# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Code Jam 2014 Round 2 - Problem C. Don't Break The Nile
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000432fed/0000000000433109
#
# Time:  O(B^2)
# Space: O(B)
#

from collections import defaultdict

def interval_dist(a1, a2, b1, b2):
    return b1-a2 if a2 < b1 else a1-b2 if b2 < a1 else 0

def distance(a, b):
    dx = interval_dist(a[0], a[2], b[0], b[2])
    dy = interval_dist(a[1], a[3], b[1], b[3])
    return max(dx, dy)-1

def dont_break_the_nile():
    W, H, B = map(int, raw_input().strip().split())

    rects = set(tuple(map(int, raw_input().strip().split())) for _ in xrange(B))
    src = (-1, 0, -1, H-1)
    dst = (W, 0, W, H-1)
    rects.add(src)
    rects.add(dst)
    dist = defaultdict(lambda: float("inf"))
    dist[src] = 0
    while rects:
        r = min(rects, key=lambda x: dist[x])
        if r == dst:
            break
        rects.remove(r)
        for rect in rects:
            d = dist[r]+distance(r, rect)
            if d < dist[rect]:
                dist[rect] = d
    return dist[dst]

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, dont_break_the_nile())
