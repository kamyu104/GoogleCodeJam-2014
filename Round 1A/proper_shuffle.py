# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Code Jam 2014 Round 1A - Problem C. Proper Shuffle
# https://code.google.com/codejam/contest/2984486/dashboard#s=p2
#
# Time:  precompute: O(N^2)
#        classify:   O(N) 
# Space: O(N^2)
#

from math import log

def proper_shuffle():
    N = input()  # N is 1000 for each case
    S = map(int, raw_input().strip().split())
    log_good_prob, log_bad_prob = -N*log(N), 0.0
    for i in xrange(N):
        log_bad_prob += log(f[S[i]][i])  # avoid prob underflow by log
    return "GOOD" if log_good_prob > log_bad_prob else "BAD"

N = 1000
P_MOVE = 1.0/N
P_STAY = 1.0-P_MOVE
dp1 = [[float(i == j) for j in xrange(N)] for i in xrange(N)]
dp2 = [0.0]*N
for i in xrange(N):
    p_stay_to_the_power_k = 1.0
    for k in xrange(N):
        dp2[i] += dp1[i][k] * p_stay_to_the_power_k * P_MOVE
        p_stay_to_the_power_k *= P_STAY
        dp1[i][k] = (P_MOVE-dp2[i]) / p_stay_to_the_power_k
f = [[dp1[i][j] * p_stay_to_the_power_k + dp2[i] for j in xrange(N)] for i in xrange(N)]
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, proper_shuffle())
