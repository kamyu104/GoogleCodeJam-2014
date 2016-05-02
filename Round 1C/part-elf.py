# Copyright (c) 2016 kamyu. All rights reserved.
#
# Google Code Jam 2016 Round 1C - Problem A. Part Elf
# https://code.google.com/codejam/contest/3004486/dashboard#s=p0
#
# Time:  O(logn)
# Space: O(1)
#

from fractions import gcd

def part_elf():
    P, Q = map(int, raw_input().strip().split('/'))
    GCD = gcd(P, Q)
    P /= GCD
    Q /= GCD
    ans = 0
    if Q > 0 and (Q & (Q - 1)) == 0:
        while Q > 1:
            if P == 1:
                ans += 1
            else:
                P /= 2
            Q /= 2
        return ans

    return "impossible"

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, part_elf())
