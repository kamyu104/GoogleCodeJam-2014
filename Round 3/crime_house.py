# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Code Jam 2014 Round 3 - Problem C. Crime House
# https://codingcompetitions.withgoogle.com/codejam/round/000000000043371f/00000000004331cb
#
# Time:  O(N^2 * logN)
# Space: O(N)
#

from collections import defaultdict
from functools import partial

def binary_search(left, right, check):
    while left <= right:
        mid = left + (right-left)//2
        if check(mid):
            right = mid-1
        else:
            left = mid+1
    return left

def check(logs, S):  # Time: O(N^2), Space: O(N)
    seq = max(x for _, x in logs)+1
    events = defaultdict(list)
    for i in reversed(xrange(len(logs))):
        if not logs[i][1]:
            continue
        events[logs[i][1]].append(i)
    outside, inside = set(events.iterkeys()), set()
    for t, x in [('E', 0)]*S + logs:
        if x:
            events[x].pop()
            if not events[x]:
                del events[x]
        if t == 'E':
            if not x:  # case 'E 0'
                i = min([events[x][-1] for x in outside if x in events and logs[events[x][-1]][0] == 'L'] or [-1])  # case 'E 0' (a)
                if i != -1:
                    x = logs[i][1]
                else:  # case 'E 0' (b)
                    x = seq  # generate a new distinct criminal id
                    seq += 1
                    outside.add(x)
            elif x in inside:  # case 'E X'
                return False
            outside.remove(x)
            inside.add(x)
        else:
            if not x:  # case 'L 0'
                i = min([events[x][-1] for x in inside if x in events and logs[events[x][-1]][0] == 'E'] or [-1])  # case 'L 0' (a)
                if i != -1:
                    x = logs[i][1]
                else:
                    x = next(iter(x for x in inside if x not in events), 0)  # case 'L 0' (b)
                    if not x:
                        i = max([events[x][-1] for x in inside if x in events and logs[events[x][-1]][0] == 'L'] or [-1])  # case 'L 0' (c)
                        if i != -1:
                            x = logs[i][1]
                        else:
                            return False
            elif x not in inside:  # case 'L X'
                return False
            inside.remove(x)
            outside.add(x)
    return True

def crime_house():
    N = input()
    logs = []
    for _ in xrange(N):
        t, x = raw_input().strip().split()
        logs.append((t, int(x)))

    S = binary_search(0, N, partial(check, logs))
    return S+sum(1 if t == 'E' else -1 for t, _ in logs) if S != N+1 else "CRIME TIME"

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, crime_house())
