# Copyright (c) 2016 kamyu. All rights reserved.
#
# Google Code Jam 2016 Round 1B - Problem A. The Repeater
# https://code.google.com/codejam/contest/2994486/dashboard#s=p0
#
# Time:  O(X * N), N is the number of strings,
#                  X is the number of characters in the frequency string.
# Space: O(X * N)
#

from random import randint

def find_kth_largest(nums, k):
    def partition_around_pivot(left, right, pivot_idx, nums):
        pivot_value = nums[pivot_idx]
        new_pivot_idx = left
        nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
        for i in xrange(left, right):
            if nums[i] > pivot_value:
                nums[i], nums[new_pivot_idx] = nums[new_pivot_idx], nums[i]
                new_pivot_idx += 1
            
        nums[right], nums[new_pivot_idx] = nums[new_pivot_idx], nums[right]
        return new_pivot_idx

    left, right = 0, len(nums) - 1
    while left <= right:
        pivot_idx = randint(left, right)
        new_pivot_idx = partition_around_pivot(left, right, pivot_idx, nums)
        if new_pivot_idx == k - 1:
            return nums[new_pivot_idx]
        elif new_pivot_idx > k - 1:
            right = new_pivot_idx - 1
        else:  # new_pivot_idx < k - 1.
            left = new_pivot_idx + 1


def run_length_encoding(s):
    encode_str = [[1, s[0]]]
    for i in xrange(1, len(s)):
        if s[i] != encode_str[-1][1]:
            encode_str.append([1, s[i]])
        else:
            encode_str[-1][0] += 1
    return encode_str


def the_repeater():
    strs = []
    for _ in xrange(input()):
        strs.append(run_length_encoding(raw_input().strip()))

    for s in strs:
        if len(s) != len(strs[0]):
            return "Fegla Won"
        for i in xrange(len(s)):
            if s[i][1] != strs[0][i][1]:
                return "Fegla Won"

    move = 0
    for j in xrange(len(strs[0])):  # X times.
        freqs = [strs[i][j][0] for i in xrange(len(strs))]  # N times.

        # Median minimizes the sum of absolute deviations.
        # freqs.sort()  # O(NlogN)
        # median = freqs[len(freqs)/2]
        median = find_kth_largest(freqs, len(freqs)/2 + 1)  # O(N) on average.

        for freq in freqs:
            move += abs(freq - median)

    return move
    
    
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, the_repeater())
