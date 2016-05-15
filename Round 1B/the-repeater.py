# Copyright (c) 2016 kamyu. All rights reserved.
#
# Google Code Jam 2016 Round 1B - Problem A. The Repeater
# https://code.google.com/codejam/contest/2994486/dashboard#s=p0
#
# Time:  O(X * NlogN), N is the number of strings,
#                      X is the number of characters.
# Space: O(X * N)
#

# Run-length Encoding.
def encode(s):
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
        strs.append(encode(raw_input().strip()))

    for str in strs:
        if len(str) != len(strs[0]):
            return "Fegla Won"
        for i in xrange(len(str)):
            if str[i][1] != strs[0][i][1]:
                return "Fegla Won"

    move = 0
    for j in xrange(len(strs[0])):  # X times.
        freqs = [strs[i][j][0] for i in xrange(len(strs))]  # N times.
        freqs.sort()  # NlogN times
        # Median minimizes the sum of absolute deviations.
        median = freqs[len(freqs)/2]
        for freq in freqs:
            move += abs(freq - median)

    return move
    
    
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, the_repeater())
