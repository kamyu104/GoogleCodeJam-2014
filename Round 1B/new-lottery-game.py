# Copyright (c) 2016 kamyu. All rights reserved.
#
# Google Code Jam 2016 Round 1B - Problem B. New Lottery Game
# https://code.google.com/codejam/contest/2994486/dashboard#s=p1
#
# Time:  O(log(max(A, B)))
# Space: O(log(max(A, B)))
#

lookup = {}
def f(A, B, K):
    if (A, B, K) in lookup:
        return lookup[(A, B, K)]

    # f(A, B, K) = 0 if 0 in (A, B, K)
    if A == 0 or B == 0 or K == 0:
        lookup[(A, B, K)] = 0
        return 0
    #  f(1, 1, K) = 1
    if A == B == 1:
        lookup[(A, B, K)] = 1
        return 1

    # f(A, B, K) is the sum of the sizes of the following 4 sets:
    #   1. {(a/2, b/2) | (a, b) in (S(A, B, K) && a even && b even)}
    #      = S(ceil(A/2), ceil(B/2), ceil(K/2))
    #   2. {(a/2, (b-1)/2) | (a, b) in (S(A, B, K) && a even && b odd)}
    #      = S(ceil(A/2), floor(B/2), ceil(K/2))
    #   3. {((a-1)/2, b/2) | (a, b) in (S(A, B, K) && a odd && b even)}
    #      = S(floor(A/2), ceil(B/2), ceil(K/2))
    #   4. {((a-1)/2, (b-1)/2) | (a, b) in (S(A, B, K) && a odd && b odd)}
    #      = S(floor(A/2), floor(B/2), floor(K/2))
    #
    # Besides:
    # - ceil(A/2) = (A+1) / 2
    # - floor(A/2) = A / 2
    #
    lookup[(A, B, K)] = f((A+1)>>1, (B+1)>>1, (K+1)>>1) + \
                        f((A+1)>>1, B>>1, (K+1)>>1) + \
                        f(A>>1, (B+1)>>1, (K+1)>>1) + \
                        f(A>>1, B>>1, K>>1)
    return lookup[(A, B, K)]


def new_lottery_game():
    A, B, K = map(int, raw_input().strip().split())
    return f(A, B, K)
    
    
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, new_lottery_game())
