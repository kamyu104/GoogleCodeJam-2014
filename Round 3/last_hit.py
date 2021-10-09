# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Code Jam 2014 Round 3 - Problem B. Last Hit
# https://codingcompetitions.witH_Google.com/codejam/round/000000000043371f/0000000000433a3e
#
# Time:  O(N^2 * MAX_H/Q)
# Space: O(N * MAX_H/Q)
#

from collections import defaultdict

def ceil_divide(a, b):
    return (a+(b-1))//b

def last_hit():
    P, Q, N = map(int, raw_input().strip().split())
    H_G = [map(int, raw_input().strip().split()) for _ in xrange(N)]

    dp = defaultdict(int)  # dp[i]: max amount of gold with i free shots
    dp[1] = 0
    for H, G in H_G:
        cnt = ceil_divide(H, Q)-1
        new_dp = defaultdict(int)
        for i, v in dp.iteritems():
            new_dp[i+cnt+1] = v
        free = cnt-ceil_divide(H-Q*cnt, P)
        for i, v in dp.iteritems():
            if i+free >= 0:
                new_dp[i+free] = max(new_dp[i+free], v+G)
        dp = new_dp
    return max(dp.itervalues())

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, last_hit())
