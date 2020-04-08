# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Code Jam 2014 Round 1A - Problem A. Charging Chaos
# https://code.google.com/codejam/contest/2984486/dashboard#s=p0
#
# Time:  O(N^2)
# Space: O(N)
#

def popcount(n):
    result = 0
    while n:
        n &= n-1
        result += 1
    return result

def charging_chaos():
    N, L = map(float, raw_input().strip().split())
    OUTLETS = map(lambda x : int(x, 2), raw_input().strip().split())
    DEVICES = set(map(lambda x : int(x, 2), raw_input().strip().split()))
    result = float("inf")
    for i, outlet in enumerate(OUTLETS):
        flips = next(iter(DEVICES))^outlet
        if set(x^flips for x in OUTLETS) == DEVICES:
            result = min(result, popcount(flips))
    return "NOT POSSIBLE" if result == float("inf") else result

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, charging_chaos())
