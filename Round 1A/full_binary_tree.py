# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Code Jam 2014 Round 1A - Problem B. Full Binary Tree
# https://code.google.com/codejam/contest/2984486/dashboard#s=p1
#
# Time:  O(N)
# Space: O(N)
#

from sys import setrecursionlimit
from collections import defaultdict

class TreeNode(object):
    def __init__(self):
        self.children = []
        self.top3 = []

def precompute_max_subtree_nodes(G, i, parent, nodes):
    for j in G[i]:
        if j == parent:
            continue
        nodes[i].children.append(j)
        nodes[i].top3.append((precompute_max_subtree_nodes(G, j, i, nodes), j))
        nodes[i].top3.sort(reverse=True)
        if len(nodes[i].top3) > 3:
            nodes[i].top3.pop()
    return 1+sum(zip(*(nodes[i].top3))[0][:2]) if len(nodes[i].top3) >= 2 else 1

def max_subtree_nodes(nodes, i, parent):
    if parent:
        parent_top3 = [(subtree_count, j) for subtree_count, j in nodes[parent].top3 if j != i]
        nodes[i].top3.append((1+sum(zip(*(parent_top3))[0][:2]) if len(parent_top3) >= 2 else 1, parent))
        nodes[i].top3.sort(reverse=True)
        if len(nodes[i].top3) > 3:
            nodes[i].top3.pop()
    result = 1+sum(zip(*(nodes[i].top3))[0][:2]) if len(nodes[i].top3) >= 2 else 1
    for j in nodes[i].children:
        result = max(result, max_subtree_nodes(nodes, j, i))
    return result

def full_binary_tree():
    N = input()
    G = defaultdict(list)
    for i in xrange(N-1):
        X, Y = map(int, raw_input().strip().split())
        G[X].append(Y)
        G[Y].append(X)
    nodes = defaultdict(TreeNode)
    precompute_max_subtree_nodes(G, 1, 0, nodes)
    return N-max_subtree_nodes(nodes, 1, 0)

BASE = 6
MAX_N = 1000
setrecursionlimit(BASE+1+MAX_N)
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, full_binary_tree())
