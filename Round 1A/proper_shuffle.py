# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Code Jam 2014 Round 1A - Problem C. Proper Shuffle
# https://code.google.com/codejam/contest/2984486/dashboard#s=p2
#
# Time:  precompute: O(N^2)
#        classify:   O(N) 
# Space: O(N^2)
#

from sys import stderr
from math import log

def proper_shuffle():
    N = input()
    S = map(int, raw_input().strip().split())
    log_good_prob, log_bad_prob = -N*log(N), 0.0
    for i in xrange(N):
        log_bad_prob += log(f[S[i]][i])
    return "GOOD" if log_good_prob > log_bad_prob else "BAD"

MAX_N = 1000
P_MOVE = 1.0/MAX_N
P_STAY = 1.0-P_MOVE
f = [[float(i == j) for j in xrange(MAX_N)] for i in xrange(MAX_N)]
g, h = [1.0]*MAX_N, [0.0]*MAX_N
for k in xrange(MAX_N):
    for i in xrange(MAX_N):
        h[i] += g[i]*f[i][k]*P_MOVE
        g[i] *= P_STAY
        f[i][k] = (P_MOVE-h[i]) / g[i]
for i in xrange(MAX_N):
    for j in xrange(MAX_N):
        f[i][j] = g[i]*f[i][j] + h[i]
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, proper_shuffle())
