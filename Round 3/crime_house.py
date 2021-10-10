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

def check(infos, seq, events, S):  # Time: O(N^2), Space: O(N)
    evts = {k:v[::-1] for k, v in events.iteritems()}
    inside, known = set(), set(events.iterkeys())
    for e, p in [('E', 0)]*S + infos:
        if e == 'E':
            chosen = False
            if not p:
                chosen = True
                i = min([evts[x][-1] for x in known if x not in inside and x in evts and infos[evts[x][-1]][0] == 'L'] or [-1])
                if i != -1:
                    p = infos[i][1]
                else:
                    p = seq
                    seq += 1
                    known.add(p)
            if p in inside:
                return False
            inside.add(p)
            if not chosen:
                if p in evts:
                    evts[p].pop()
                    if not evts[p]:
                        del evts[p]
        else:
            chosen = False
            if not p:
                chosen = True
                i = min([evts[x][-1] for x in inside if x in evts and infos[evts[x][-1]][0] == 'E'] or [-1])
                if i != -1:
                    p = infos[i][1]
                else:
                    p = next(iter(x for x in inside if x not in evts), 0)
                    if not p:
                        i = max([evts[x][-1] for x in inside if x in evts and infos[evts[x][-1]][0] == 'L'] or [-1])
                        if i != -1:
                            p = infos[i][1]
                        else:
                            return False
            if p not in inside:
                return False
            inside.remove(p)
            if not chosen:
                if p in evts:
                    evts[p].pop()
                    if not evts[p]:
                        del evts[p]
    return True

def crime_house():
    N = input()
    infos = []
    for _ in xrange(N):
        e, p = raw_input().strip().split()
        infos.append((e, int(p)))

    seq = max(p for _, p in infos)+1
    events = defaultdict(list)
    for i, (e, p) in enumerate(infos):
        if not p:
            continue
        events[p].append(i)
    S = binary_search(0, N, partial(check, infos, seq, events))
    if S == N+1:
        return "CRIME TIME"
    return S+sum(1 if e == 'E' else -1 for e, _ in infos)

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, crime_house())
