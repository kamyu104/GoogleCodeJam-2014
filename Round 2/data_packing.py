# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Code Jam 2014 Round 2 - Problem A. Data Packing
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000432fed/0000000000432b8d
#
# Time:  O(NlogN)
# Space: O(1)
#

def data_packing():
    N, X = map(int, raw_input().strip().split())
    S = map(int, raw_input().strip().split())

    S.sort()
    result = 0
    left, right = 0, len(S)-1
    while left <= right:
        if left < right and S[left]+S[right] <= X:
            left += 1
        right -= 1
        result += 1
    return result

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, data_packing())
