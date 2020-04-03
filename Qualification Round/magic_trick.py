# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Code Jam 2014 Qualification Round - Problem A. Magic Trick
# https://code.google.com/codejam/contest/2974486/dashboard#s=p0
#
# Time:  O(1)
# Space: O(1)
#

def magic_trick():
    ANS, ARR = [0]*2, [[] for _ in xrange(2)]
    for i in xrange(2):
        ANS[i] = input()-1
        for _ in xrange(4):
            ARR[i].append(map(int, raw_input().strip().split()))
    result = set(ARR[0][ANS[0]]) & set(ARR[1][ANS[1]])
    if not result:
        return "Volunteer cheated!"
    if len(result) > 1:
        return "Bad magician!"
    return result.pop()

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, magic_trick())
