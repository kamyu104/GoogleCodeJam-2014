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
p_stay_to_the_power = [1.0]
for i in xrange(N-1):
    p_stay_to_the_power.append(p_stay_to_the_power[-1]*P_STAY)
accu = [[0.0]*N for _ in xrange(N)]
for i in xrange(N):
    for j in xrange(N):
        accu[i][j] = accu[i][j-1] + (i == j) * p_stay_to_the_power[i]
f = [[((1.0-accu[i][j]) * p_stay_to_the_power[N-1-j] + accu[i][N-1]) * P_MOVE
       for j in xrange(N)] for i in xrange(N)]
assert(sum(map(lambda x: sum(x), f))/N == 1.0)
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, proper_shuffle())
