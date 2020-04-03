# Copyright (C) 2020 kamyu. All rights reserved.
#
# Google Code Jam 2014 Qualification Round - Problem D. Deceitful War
# https://code.google.com/codejam/contest/2974486/dashboard#s=p3
#
# Time:  O(NlogN)
# Space: O(N)
#

def accumulate(iterator):
    total = 0
    for item in iterator:
        total += item
        yield total

def deceitful_war():
    N = input()
    blocks = [(float(i), -1) for i in raw_input().strip().split()]
    blocks += [(float(i), 1) for i in raw_input().strip().split()]
    blocks.sort()
    accu = list(accumulate(zip(*blocks)[1]))
    return "{} {}".format(N+min(accu), max(accu))

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, deceitful_war())
