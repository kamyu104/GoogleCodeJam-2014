# Copyright (c) 2016 kamyu. All rights reserved.
#
# Google Code Jam 2016 Round 1C - Problem A. Part Elf
# https://code.google.com/codejam/contest/3004486/dashboard#s=p0
#
# Time:  O(logQ)
# Space: O(1)
#

from fractions import gcd

def part_elf():
    P, Q = map(int, raw_input().strip().split('/'))
    GCD = gcd(P, Q)
    P //= GCD
    Q //= GCD
    if Q > 0 and (Q & (Q - 1)) == 0:  # Q is power of 2.
        gen = 0
        while P < Q:
            P *= 2
            gen += 1
        return gen

    return "impossible"


for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, part_elf())
