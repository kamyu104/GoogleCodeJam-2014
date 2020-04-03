# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Code Jam 2014 Qualification Round - Problem B. Cookie Clicker Alpha
# https://code.google.com/codejam/contest/2974486/dashboard#s=p1
#
# Time:  O(X / C)
# Space: O(1)
#

def cookie_clicker_alpha():
    C, F, X = map(float, raw_input().strip().split())
    result, rate = 0.0, 2.0
    # rate >= F*X/C - F => times of loop >= X/C - 1 - 2/F
    while C/rate+X/(rate+F) < X/rate:
        result += C/rate
        rate += F
    return result + X/rate

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, cookie_clicker_alpha())
