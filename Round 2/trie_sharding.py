# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Code Jam 2014 Round 2 - Problem D. Trie Sharding
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000432fed/0000000000432f41
#
# Time:  O(T * N^2), T is the number of nodes in trie
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

def count(cnts, n):  # Time: O(N^2)
    dp = {}
    for i in xrange(1, n+1):
        dp[i] = 1
        for k in cnts:  # Time: O(26)
            dp[i] = mulmod(dp[i], nCr(i, k))  # all possible count
        for j in xrange(1, i):
            dp[i] = submod(dp[i], mulmod(dp[j], nCr(i, i-j)))  # substract count of j non-empty servers and (i-j) empty servers for j in [1, i-1]
    return dp[n]

def trie_sharding():
    M, N = map(int, raw_input().strip().split())
    S = [raw_input().strip() for _ in xrange(M)]

    trie = [{}]
    end_nodes = set()
    for s in S:
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
        cnt[i] = int(i in end_nodes)
        cnts = [cnt[j] for j in trie[i].itervalues()]
        if i in end_nodes:
            cnts.append(1)
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
