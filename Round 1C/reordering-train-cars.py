# Copyright (c) 2016 kamyu. All rights reserved.
#
# Google Code Jam 2016 Round 1C - Problem B. Reordering Train Cars
# https://code.google.com/codejam/contest/3004486/dashboard#s=p1
#
# Time:  O(L), L is the set of connected Cars' length.
# Space: O(1)
#

from collections import defaultdict

# Collapse strings.
def collapse(s):
    chars = list(s)
    collapsed_chars = [chars[0]]
    for i in xrange(1, len(chars)):
        if chars[i] != collapsed_chars[-1]:
            collapsed_chars += chars[i]
    return "".join(collapsed_chars)


def reordering_train_cars():
    N = int(input())
    cars = map(collapse, raw_input().strip().split())
    
    begin, end, middle, single_chars = {}, {}, {}, defaultdict(int)
    for i, s in enumerate(cars):
        if len(s) == 1:
            single_chars[s[0]] += 1
        else:
            # There is no letter repeated in
            # two different places in the string.
            if s[0] == s[-1]:
                return 0

            # It appears at most once in the
            # beginning of one string.
            if s[0] in begin:
                return 0
            else:
                begin[s[0]] = i

            # It appears at most once at the
            # end of one string.
            if s[-1] in end:
                return 0
            else:
                end[s[-1]] = i

            # It appears in the middle of one string,
            # and nowhere else.
            for j in xrange(1, len(s) - 1):
                if any([s[j] in begin, \
                        s[j] in end, \
                        s[j] in middle]):
                    return 0
                else:
                    middle[s[j]] = i

    # It appears any number of times as
    # a single-character string.
    num_groups, ways = 0, 1
    for c in single_chars.keys():
        ways = (ways * factorials[single_chars[c]]) % MOD
        if c not in begin and c not in end:
            num_groups += 1

    while begin:
        # Form each disjoint group.
        _, i = begin.popitem()
        front, back = cars[i][0], cars[i][-1]
        del end[back]

        while back in begin:
            back = cars[begin.pop(back)][-1]
            del end[back]
        
        while front in end:
            front = cars[end.pop(front)][0]
            del begin[front]

        # All occurrences of the same character
        # should be adjacent to each other.
        if front == back:
            return 0

        num_groups += 1
    
    ways = (ways * factorials[num_groups]) % MOD
    
    return ways


MOD = int(1e9 + 7)

# Precompute factorials.
factorials = [1]
for i in xrange(1, 101):
    factorials.append((factorials[-1] * i) % MOD)

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, reordering_train_cars())

