# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Code Jam 2014 Round 2 - Problem B. Up And Down
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000432fed/000000000043333d
#
# Time:  O(NlogN)
# Space: O(N)
#

# Template:
# https://github.com/kamyu104/LeetCode-Solutions/blob/master/Python/range-sum-query-mutable.py
class BIT(object):  # 0-indexed.
    def __init__(self, nums):
        self.__bit = [0]*(len(nums)+1)  # Extra one for dummy node.
        for i in xrange(1, len(self.__bit)):
            self.__bit[i] = nums[i-1] + self.__bit[i-1]
        for i in reversed(xrange(1, len(self.__bit))):
            last_i = i - (i & -i)
            self.__bit[i] -= self.__bit[last_i]

    def add(self, i, val):
        i += 1  # Extra one for dummy node.
        while i < len(self.__bit):
            self.__bit[i] += val
            i += (i & -i)

    def query(self, i):
        i += 1  # Extra one for dummy node.
        ret = 0
        while i > 0:
            ret += self.__bit[i]
            i -= (i & -i)
        return ret

def up_and_down():
    N = input()
    A = map(int, raw_input().strip().split())

    num_to_idx = {x:i for i, x in enumerate(A)}
    A.sort()
    bit = BIT([1]*len(A))
    result = 0
    for rank, x in enumerate(A):
        i = num_to_idx[x]
        cnt = bit.query(i)
        result += min(cnt-1, (len(A)-rank)-cnt)
        bit.add(i, -1)
    return result

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, up_and_down())
