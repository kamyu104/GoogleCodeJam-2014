# Copyright (c) 2016 kamyu. All rights reserved.
#
# Google Code Jam 2014 Round 3 - Problem A. Magical, Marvelous Tour
# https://codingcompetitions.withgoogle.com/codejam/round/000000000043371f/000000000043380e
#
# Time:  O(N)
# Space: O(N)
#

def magical_marvelous_tour():
    N, p, q, r, s = map(int, raw_input().strip().split())
    D = [(i*p+q)%r+s for i in xrange(N)]

    result = total = sum(D)
    left, mid, right = 0, 0, total
    i = 0
    for j in xrange(N):
        right -= D[j]
        mid += D[j]
        while i+1 < j+1 and max(left+D[i], mid-D[i], right) < max(left, mid, right):
            mid -= D[i]
            left += D[i]
            i += 1
        result = min(result, max(left, mid, right))
    return float(total-result)/total

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, magical_marvelous_tour())
