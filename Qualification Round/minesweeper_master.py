# Copyright (C) 2020 kamyu. All rights reserved.
#
# Google Code Jam 2014 Qualification Round - Problem C. Minesweeper Master
# https://code.google.com/codejam/contest/2974486/dashboard#s=p2
#
# Time:  O(R * C)
# Space: O(1)
#

def minesweeper_master():
    R, C, M = map(int, raw_input().strip().split())
    result, empty = [['*']*C for _ in xrange(R)], R*C - M
    if empty == 1:
        pass
    elif R == 1 or C == 1:
        for i in xrange(empty):
            if R == 1:
                result[0][i] = '.'
            else:
                result[i][0] = '.'
    elif (R == 2 or C == 2) and (empty != 2 and not empty%2):
        for i in xrange(empty//2):
            if R == 2:
                result[0][i] = '.'
                result[1][i] = '.'
            else:
                result[i][0] = '.'
                result[i][1] = '.'
    elif (R >= 3 and C >= 3) and (empty == 4 or empty == 6 or empty >= 8):
        if empty < 2*C+2:
            for i in xrange(empty//2):
                result[0][i] = '.'
                result[1][i] = '.'
            if empty%2:
                result[2][0] = '.'
                result[2][1] = '.'
                result[2][2] = '.'
                result[0][empty//2-1] = '*'
                result[1][empty//2-1] = '*'
        else:
            for i in xrange(R):
                for j in xrange(max(min(empty-C*i, C), 0)):
                    result[i][j] = '.'
            if empty%C == 1:
                result[empty//C][1] = '.'
                result[empty//C-1][C-1] = '*'
    else:
        return "Impossible"
    result[0][0] = 'c'
    return "\n".join(map(lambda result: "".join(result), result))

for case in xrange(input()):
    print 'Case #%d: \n%s' % (case+1, minesweeper_master())
