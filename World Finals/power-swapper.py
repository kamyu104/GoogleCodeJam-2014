# Copyright (c) 2015 kamyu. All rights reserved.
#
# Google Code Jam 2014 World Finals - Problem B. Power Swapper
# https://code.google.com/codejam/contest/7214486/dashboard#s=p1
#
# Time:  O(2^(N*2))
# Space: O(2^N)
#

import math

def swap(arr, i, j, sz):  # Swap two sets.
    for k in xrange(sz):
        t = arr[i + k]
        arr[i + k] = arr[j + k]
        arr[j + k] = t


def count(arr, N, k, nswapped):
    if k == N:
        return math.factorial(nswapped)

    i = 0
    idx = []  # Candidates' index for swappings.
    sz = 2**k
    while i < 2**N:
        if arr[i] + sz != arr[i + sz]:
            idx.append(i)
        i = i + sz * 2

    ret = 0
    if len(idx) == 0:  # No swap needed.
        ret = count(arr, N, k + 1, nswapped)

    elif len(idx) == 1:  # Only one choice to swap.
        swap(arr, idx[0], idx[0] + sz, sz)
        if arr[idx[0]] + sz == arr[idx[0] + sz]:
            ret = count(arr, N, k + 1, nswapped + 1)
        swap(arr, idx[0], idx[0] + sz, sz)

    elif len(idx) == 2:  # At most 2 choices.
        for i in [idx[0], idx[0] + sz]:
            for j in [idx[1], idx[1] + sz]:
                swap(arr, i, j, sz)
                if arr[idx[0]] + sz == arr[idx[0] + sz]:
                    if arr[idx[1]] + sz == arr[idx[1] + sz]:
                        ret += count(arr, N, k + 1, nswapped + 1)
                swap(arr, i, j, sz)

    return ret


for case in xrange(input()):
    N = input()
    arr = map(int, raw_input().strip().split())
    print "Case #%d: %d" % (case+1, count(arr, N, 0, 0))
