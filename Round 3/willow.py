# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Code Jam 2014 Round 3 - Problem D. Willow
# https://codingcompetitions.withgoogle.com/codejam/round/000000000043371f/00000000004336d0
#
# Time:  O(N^2)
# Space: O(N^2)
#

from sys import setrecursionlimit
from collections import defaultdict
from heapq import heappush, heappop

# precompute next_node_to, best_coins, best_nodes
def dfs(C, adj, edge_id, i, pi, start, first_node, next_node_to, best_coins, best_nodes):  # Time: O(N)
    next_node_to[start][i] = first_node
    for ni in adj[i]:
        if ni != pi:
            dfs(C, adj, edge_id, ni, i, start, first_node, next_node_to, best_coins, best_nodes)
    best_coins[edge_id[i][pi]] = C[i]+max([best_coins[edge_id[ni][i]] for ni in adj[i] if ni != pi] or [0])
    min_heap = []
    for ni in adj[i]:  # Total Time: O(N * logK) = O(N)
        if ni == pi:
            continue
        heappush(min_heap, (best_coins[edge_id[ni][i]], ni))
        if len(min_heap) == K+1:
            heappop(min_heap)
    while min_heap:
        best_nodes[edge_id[i][pi]].append(heappop(min_heap)[1])

# return the best next vertex when coming from edge (pi to i), excluding vertex in exlude
def next_best_except(edge_id, best_nodes, i, pi, exclude):
    return next(iter(x for x in reversed(best_nodes[edge_id[i][pi]]) if x not in exclude), -1)

# max coins for subtree i with parent pi
def max_coins(edge_id, best_coins, i, pi):
    return 0 if i < 0 else best_coins[edge_id[i][pi]]

# max coins for the other player branching off at any vertex in [i, j]
def memoization2(C, edge_id, next_node_to, best_coins, best_nodes, i, pi, j, pj, lookup2):  # Time: O(N^2)
    ei, ej = edge_id[i][pi], edge_id[j][pj]
    if lookup2[ei][ej] == -1:
        if i == j:
            ni = next_best_except(edge_id, best_nodes, i, pi, {pj})  # the current player pick the next best path
            nj = next_best_except(edge_id, best_nodes, i, pi, {pj, ni})  # the other player pick the next next best path
            lookup2[ei][ej] = max_coins(edge_id, best_coins, nj, j)
        else:
            nj = next_node_to[j][i]
            branch_off_later = (0 if nj == i else C[nj]) + memoization2(C, edge_id, next_node_to, best_coins, best_nodes, i, pi, nj, j, lookup2)
            nj = next_best_except(edge_id, best_nodes, j, pj, {nj})
            branch_off_now = max_coins(edge_id, best_coins, nj, j)
            lookup2[ei][ej] = max(branch_off_later, branch_off_now)
    return lookup2[ei][ej]

# minimax for the current player with last edge (pi to i) and the other player with last edge (pj to j)
def memoization(C, edge_id, next_node_to, best_coins, best_nodes, i, pi, j, pj, lookup, lookup2):  # Time: O(N^2)
    ei, ej = edge_id[i][pi], edge_id[j][pj]
    if lookup[ei][ej] == -1:
        if i == j:
            ni = next_best_except(edge_id, best_nodes, i, pi, {pj})  # the current player pick the next best path
            nj = next_best_except(edge_id, best_nodes, i, pi, {pj, ni})  # the other player pick the next next best path
            lookup[ei][ej] = max_coins(edge_id, best_coins, ni, i) - max_coins(edge_id, best_coins, nj, j)
        else:
            ni = next_node_to[i][j]
            branch_off_later = (0 if ni == j else C[ni]) - memoization(C, edge_id, next_node_to, best_coins, best_nodes, j, pj, ni, i, lookup, lookup2)
            ni = next_best_except(edge_id, best_nodes, i, pi, {ni})
            branch_off_now = max_coins(edge_id, best_coins, ni, i) - memoization2(C, edge_id, next_node_to, best_coins, best_nodes, i, pi, j, pj, lookup2)
            lookup[ei][ej] = max(branch_off_later, branch_off_now)
    return lookup[ei][ej]

def willow():
    N = input()
    C = [input() for _ in xrange(N)]
    adj = defaultdict(list)
    edge_id = [[-1 for _ in xrange(N+1)] for _ in xrange(N+1)]  # edge_id[j][i]: id of edge (i to j)
    seq = 0
    for i in xrange(N-1):
        j = input()-1
        adj[i].append(j)
        adj[j].append(i)
        edge_id[i][j] = seq
        seq += 1
        edge_id[j][i] = seq
        seq += 1
    for i in xrange(N):
        edge_id[i][N] = seq
        seq += 1

    # precompute
    next_node_to = [[-1 for _ in xrange(N+1)] for _ in xrange(N+1)]
    best_coins = [0 for _ in xrange(seq)]
    best_nodes = [[] for _ in xrange(seq)]
    for i in xrange(N):  # Time: O(N^2)
        dfs(C, adj, edge_id, i, N, N, i, next_node_to, best_coins, best_nodes)
        for j in adj[i]:
            dfs(C, adj, edge_id, j, i, i, j, next_node_to, best_coins, best_nodes)

    lookup = [[-1 for _ in xrange(seq)] for _ in xrange(seq)]
    lookup2 = [[-1 for _ in xrange(seq)] for _ in xrange(seq)]
    max_diff = float("-inf")
    for i in xrange(N):  # Time: O(N^2)
        min_diff = float("inf")
        for j in xrange(N):
            cost = C[i] - (0 if i == j else C[j])
            min_diff = min(min_diff, cost + memoization(C, edge_id, next_node_to, best_coins, best_nodes, i, N, j, N, lookup, lookup2))
        max_diff = max(max_diff, min_diff)
    return max_diff

BASE = 2
MAX_N = 500
setrecursionlimit(BASE+MAX_N)
K = 3
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, willow())
