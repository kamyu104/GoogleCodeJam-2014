# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Code Jam 2014 Round 2 - Problem D. Trie Sharding
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000432fed/0000000000432f41
#
# Time:  O(M * L + T * N^2), L is the max length of strings in S, T is the number of nodes in trie
# Space: O(T)
#

def submod(a, b):
    return (a-b)%MOD

def mulmod(a, b):
    return (a*b)%MOD

# Template:
# https://github.com/kamyu104/GoogleCodeJam-2021/blob/5f998148a7d18cb2f1f768352de63885437f6c6b/Round%202/hidden_pancakes.py
def nCr(n, k):
    if not (0 <= k <= n):
        return 0
    while len(inv) <= n:  # lazy initialization
        fact.append(fact[-1]*len(inv) % MOD)
        inv.append(inv[MOD%len(inv)]*(MOD-MOD//len(inv)) % MOD)  # https://cp-algorithms.com/algebra/module-inverse.html
        inv_fact.append(inv_fact[-1]*inv[-1] % MOD)
    return (fact[n]*inv_fact[n-k] % MOD) * inv_fact[k] % MOD

def count(cnts, n):  # Time: O(N^2), count of each server with at most one string from each subtree and at least one string
    dp = {}
    for i in xrange(1, n+1):
        dp[i] = 1
        for k in cnts:  # Time: O(26+1)
            dp[i] = mulmod(dp[i], nCr(i, k))  # all count of each server with at most one string from each subtree
        for k in xrange(1, i):
            dp[i] = submod(dp[i], mulmod(dp[k], nCr(i, k)))  # substract count of k non-empty servers and (i-k) empty servers for k in [1, i-1]
    return dp[n]

def trie_sharding():
    M, N = map(int, raw_input().strip().split())
    S = [raw_input().strip() for _ in xrange(M)]

    trie = [{}]
    end_nodes = set()
    for s in S:  # Time: O(M * L)
        curr = 0
        for c in s:
            if c not in trie[curr]:
                trie[curr][c] = len(trie)
                trie.append({})
            curr = trie[curr][c]
        end_nodes.add(curr)

    cnt = {}
    result, total = 0, 1
    for i in reversed(xrange(len(trie))):  # O(T) times
        cnts = [cnt[child] for child in trie[i].itervalues()]
        cnts.append(int(i in end_nodes))
        cnt[i] = min(sum(cnts), N)
        result += cnt[i]
        total = mulmod(total, count(cnts, cnt[i]))
    return "%s %s" % (result, total)

MOD = 10**9+7
fact = [1, 1]
inv = [0, 1]
inv_fact = [1, 1]
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, trie_sharding())
