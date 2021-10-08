# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Code Jam 2014 Round 2 - Problem A. Data Packing
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000432fed/0000000000432b8d
#
# Time:  O(N + X) = O(N + 700) = O(N)
# Space: O(X) = O(700) = O(1)
#

def inplace_counting_sort(nums, reverse=False):  # Time: O(n)
    count = [0]*(max(nums)+1)
    for num in nums:
        count[num] += 1
    for i in xrange(1, len(count)):
        count[i] += count[i-1]
    for i in reversed(xrange(len(nums))):  # inplace but unstable sort
        if nums[i] < 0:  # processed
            continue
        while i != count[nums[i]]-1:
            count[nums[i]] -= 1
            nums[count[nums[i]]], nums[i] = ~nums[i], nums[count[nums[i]]]
        count[nums[i]] -= 1
        nums[i] = ~nums[i]
    for i in xrange(len(nums)):
        nums[i] = ~nums[i]  # restore values
    if reverse:  # unstable sort
        nums.reverse()

def data_packing():
    N, X = map(int, raw_input().strip().split())
    S = map(int, raw_input().strip().split())

    inplace_counting_sort(S)
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
