# Copyright (c) 2016 kamyu. All rights reserved.
#
# Google Code Jam 2016 Round 1C - Problem B. Reordering Train Cars
# https://code.google.com/codejam/contest/3004486/dashboard#s=p1
#
# Time:  O(N)
# Space: O(1)
#

from collections import defaultdict

# Collapse strings.
def unique(s):
    r = s[0] 
    for i in xrange(1, len(s)):
        if s[i] != r[-1]:
            r += s[i]
    return r

def reordring_train_cars():
    N = int(input())
    cars = map(unique, raw_input().strip().split())
    
    single_chars, begin, end = defaultdict(int), {}, {}
    for s in cars:
        if len(s) == 1:
            single_chars[s[0]] += 1
        else:
            if s[0] in begin:
                return 0
            else:
                begin[s[0]] = s

            if s[-1] in end:
                return 0
            else:
                end[s[-1]] = s

    for s in begin.values():
        for i in xrange(1, len(s) - 1):
            if s[i] in begin or s[i] in end:
                return 0

    ways = 1
    for c in single_chars.keys():
        ways = (ways * factorials[single_chars[c]]) % MOD
        if c not in begin and c not in end:
            begin[c] = end[c] = c

    n = 0
    while len(begin) > 0:
        _, s = begin.popitem()
        del end[s[-1]]

        while s[-1] in begin:
            s += begin.pop(s[-1])
            del end[s[-1]]
        
        while s[0] in end:
            s = end.pop(s[0]) + s
            del begin[s[0]]

        if len(s) > 1 and s[0] == s[-1]:
            return 0

        n += 1
    
    ways = (ways * factorials[n]) % MOD
    
    return ways

# Precompute factorials.
MOD = int(1e9 + 7)
factorials = [1]
for i in xrange(1, 105):
    factorials.append((factorials[-1] * i) % MOD)

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, reordring_train_cars())

