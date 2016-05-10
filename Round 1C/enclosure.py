# Copyright (c) 2016 kamyu. All rights reserved.
#
# Google Code Jam 2016 Round 1C - Problem C. Enclosure
# https://code.google.com/codejam/contest/3004486/dashboard#s=p2
#
# Time:  O(N^2 * M)
# Space: O(1)
#

def empty_triangle(size):
    return size * (size + 1) / 2


def min_stones(N, M, K):
    if N > M:
        (N, M) = (M, N)
    # 1. The optimal shape resembles a dianmond:
    #   --***--
    #   -*XXX*-
    #   *XXXXX*
    #   -*XXXX*
    #   --*XX*-
    #   ---**--
    #
    # 2. The sizes (the length of its side) of
    #    the empty triangles at the corners may
    #    be different by at most one size.
    
    # Generate all possible truncated (and perfect) diamond shapes.
    res = K
    for R in xrange(2, N + 1):
        for C in xrange(R, M + 1):
            if R * C >= K:
                for i in xrange(2 * R):
                    cover = R * C
                    # Increase the size of the empty triangle
                    # at each corner.
                    cover -= empty_triangle((i + 3) // 4)
                    cover -= empty_triangle((i + 2) // 4)
                    cover -= empty_triangle((i + 1) // 4)
                    cover -= empty_triangle(i // 4)
                    if cover < K:
                        break
                    stones = 2 * (R + C) - 4 - i
                    res = min(res, stones)

    return res


def enclosure():
    N, M, K = map(int, raw_input().strip().split())
    return min_stones(N, M, K)

    
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, enclosure())
