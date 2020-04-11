# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Code Jam 2014 Round 1A - Problem C. Proper Shuffle
# https://code.google.com/codejam/contest/2984486/dashboard#s=p2
#
# Time:  precompute: O(N^3)
#        classify:   O(N) 
# Space: O(N^2)
#

from sys import stderr
from math import log

def proper_shuffle():
    N = input()
    P = map(int, raw_input().strip().split())
    z_good_prob, z_bad_prob = -N*log(N), 0.0
    for i in xrange(N):
        z_bad_prob += log(F[i][P[i]])
    return "GOOD" if z_good_prob > z_bad_prob else "BAD"

'''
MAX_N = 1000
P_MOVE = 1.0/MAX_N
P_STAY = 1.0-P_MOVE
F = [[float(i == j) for j in xrange(MAX_N)] for i in xrange(MAX_N)]
for i in xrange(MAX_N):
    print >>stderr, i
    for j in xrange(MAX_N):
        if j != i:
            for k in xrange(MAX_N):
                F[j][k] = F[j][k]*P_STAY + F[i][k]*P_MOVE
    for k in xrange(MAX_N):
        F[i][k] = P_MOVE
print >>open("proper_shuffle_precompute.txt", "w"), F
'''
F = eval(open("proper_shuffle_precompute.txt", "r").read())
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, proper_shuffle())
