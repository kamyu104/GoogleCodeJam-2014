# Copyright (c) 2015 kamyu. All rights reserved.
#
# Google Code Jam 2014 World Finals - Problem E. Allergy Testing
# https://code.google.com/codejam/contest/7214486/dashboard#s=p4
#
# Time:  O((logN)^3)
# Space: O(1)
#
# Combinatorial Solution
#

def nCk(n, k):
    if k > n:
        return 0
    res = 1
    for i in xrange(1, min(n - k, k) + 1):
        res = res * (n - i + 1) // i
    return res

def max_foods(D, A, B):
    cnt = 0
    for L in xrange(min(51, D // B + 1)):
        K_min = (D - L * B - B) // A + 1
        K_max = (D - L * B) // A
        cnt += nCk(K_max + L + 1, L + 1) - nCk(K_min + L, L + 1)
    return cnt

def min_days(N, A, B):
    left = 0
    right = int(1e15)
    while left < right:
        D = (left + right) // 2
        if max_foods(D, A, B) >= N:
            right = D
        else:
            left = D + 1
    return left

for case in xrange(input()):
    print "Case #%d: %d" % (case+1, \
        min_days(*map(int, raw_input().strip().split())))
