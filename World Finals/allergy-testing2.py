# Copyright (c) 2015 kamyu. All rights reserved.
#
# Google Code Jam 2014 World Finals - Problem E. Allergy Testing
# https://code.google.com/codejam/contest/7214486/dashboard#s=p4
#
# Time:  O(?)
# Space: O(?)
#
# Dynamic Programming Solution
#

INF = 1e16

def max_foods(D, A, B):
  ans = 0
  mem = [0] * 60  # zero-array of 60 elements.
  mem[0] = 1
  for i in xrange(D // A + 1):  # A-edges.
    for j in xrange(D // B + 1):  # B-edges.
      H = i * A + j * B  # Height of this node.

      # Skip this node if it uses more than D days.
      if H > D: break

      # Aggregate the child's value.
      if j > 0 and H + A <= D: mem[j] += mem[j-1]

      # if we are too close to D to add a B-edge,
      # the right child is a leaf,
      # so add this node to the answer.
      if H + B + A > D: ans += mem[j]

      # Avoid overflows.
      ans = min(ans, INF)
      mem[j] = min(mem[j], INF)

  return ans

def linear(D, A, B):
  return D // A + 1

def quadratic(D, A, B):
  R = (D - B) // A
  if INF / R < R: return INF
  return linear(D, A, B) + (R * (R + 1)) // 2

def cubic(D, A, B):
  ans = quadratic(D, A, B)
  a = (D - 2 * B) // A
  for i in xrange(a):
    R = a - i
    if INF / R < R: return INF
    ans += (R * (R + 1)) // 2
    if ans > INF: return INF
  return ans

def binary_search(N, A, B, low, high, func):
  while high - low > 1:
    D = (high + low) // 2
    if func(D, A, B) >= N:
      high = D
    else:
      low = D
  return high

def min_days(N, A, B):
  if quadratic(B + A, A, B) >= N:
    return binary_search(N, A, B, -1, B + A, linear)
  if cubic(2 * B + A, A, B) >= N:
    return binary_search(N, A, B, B + A, 2 * B + A, quadratic)
  if cubic(3 * B + A, A, B) + 1 >= N:
    return binary_search(N, A, B, 2 * B + A, 3 * B + A, cubic)
  return binary_search(N, A, B, 3 * B + A, 51 * B, max_foods)

for case in xrange(input()):
    print "Case #%d: %d" % (case+1, \
        min_days(*map(int, raw_input().strip().split())))