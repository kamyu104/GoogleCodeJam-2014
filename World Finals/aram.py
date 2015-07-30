# Copyright (c) 2015 kamyu. All rights reserved.
#
# Google Code Jam 2014 World Finals - Problem F. ARAM
# https://code.google.com/codejam/contest/7214486/dashboard#s=p5
#
# Time:  O(60 * N * R * G)
# Space: O(1)
#

# Can you win at least X fraction of the time?
def CanWin(X):
    A = []
    last_G_values = 0

    # C < G, not enough coins for a reroll.
    for C in xrange(0, G):
        A.append(avg_win_prob_top[N] - X)
        last_G_values += A[C]

    # C >= G, enough coins for a reroll.
    for C in xrange(G, R * G + 1):
        A.append(-1e100)
        for K in xrange(1, N + 1):
            p = 1.0 * (N - K) / N    # Probability of rerolling.
            p_reroll = p / (1 - p) * last_G_values
            p_not_reroll = avg_win_prob_top[K] - X
            A[C] = max(A[C], p_reroll + p_not_reroll)

        if A[C] >= 0:
            return True
        last_G_values += A[C] - A[C - G]

    return False


for case in xrange(input()):
    N, R, G = map(int, raw_input().strip().split())
    win_prob = map(float, raw_input().strip().split())
    win_prob = sorted(win_prob, reverse=True)

    avg_win_prob_top = [0]
    for topK in xrange(1, N + 1):
        avg_win_prob_top.append(sum(win_prob[0:topK]) / topK)

    left = 0.0
    right = 1.0
    for i in xrange(60):
        mid = (left + right) / 2
        if not CanWin(mid):
            right = mid
        else:
            left = mid
    print "Case #%d: %.15f" % (case+1, left)