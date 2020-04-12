# [GoogleCodeJam 2014](https://codingcompetitions.withgoogle.com/codejam/archive/2014) ![Language](https://img.shields.io/badge/language-Python-orange.svg) [![License](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE.md) ![Progress](https://img.shields.io/badge/progress-19%20%2F%2027-ff69b4.svg)

Python solutions of Google Code Jam 2014. Solution begins with `*` means it will get TLE in the largest data set (total computation amount > `10^8`, which is not friendly for Python to solve in 5 ~ 15 seconds). A `4-minute` timer is set for the small dataset and a `8-minute` timer is set for the large dataset this year.

* [Code Jam 2013](https://github.com/kamyu104/GoogleCodeJam-2013)
* [Qualification Round](https://github.com/kamyu104/GoogleCodeJam-2014#qualification-round)
* [Round 1A](https://github.com/kamyu104/GoogleCodeJam-2014#round-1a)
* [Round 1B](https://github.com/kamyu104/GoogleCodeJam-2014#round-1b)
* [Round 1C](https://github.com/kamyu104/GoogleCodeJam-2014#round-1c)
* [Round 2](https://github.com/kamyu104/GoogleCodeJam-2014#round-2)
* [Round 3](https://github.com/kamyu104/GoogleCodeJam-2014#round-3)
* [World Finals](https://github.com/kamyu104/GoogleCodeJam-2014#world-finals)
* [Code Jam 2015](https://github.com/kamyu104/GoogleCodeJam-2015)

## Qualification Round
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Magic Trick](https://code.google.com/codejam/contest/2974486/dashboard#s=p0)| [Python](./Qualification%20Round/magic_trick.py) | _O(1)_  | _O(1)_  | Easy | | Set |
|B| [Cookie Clicker Alpha](https://code.google.com/codejam/contest/2974486/dashboard#s=p1)| [Python](./Qualification%20Round/cookie_clicker_alpha.py) | _O(X / C)_  | _O(1)_  | Easy | | Math |
|C| [Minesweeper Master](https://code.google.com/codejam/contest/2974486/dashboard#s=p2)| [Python](./Qualification%20Round/minesweeper_master.py) | _O(R * C)_  | _O(1)_ | Medium | | Enumeration |
|D| [Deceitful War](https://code.google.com/codejam/contest/2974486/dashboard#s=p3)| [Python](./Qualification%20Round/deceitful_war.py) | _O(NlogN)_  | _O(N)_ | Medium | | Sort |

## Round 1A
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Charging Chaos](https://code.google.com/codejam/contest/2984486/dashboard#s=p0)| [Python](./Round%201A/charging_chaos.py) | _O(N^2)_  | _O(N)_  | Easy | | Bit Manipulation |
|B| [Full Binary Tree](https://code.google.com/codejam/contest/2984486/dashboard#s=p1)| [Python](./Round%201A/full_binary_tree.py)  | _O(N)_ |  _O(N)_ | Easy | | DFS, Graph, Binary Tree |
|C| [Proper Shuffle](https://code.google.com/codejam/contest/2984486/dashboard#s=p2)| [Python](./Round%201A/proper_shuffle.py) | precompute: _O(N^2)_<br>classify: _O(N)_ |  _O(N^2)_ | Medium | | Precomputation, Probability, Naive Bayes Classifier |

## Round 1B
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [The Repeater](https://code.google.com/codejam/contest/2994486/dashboard#s=p0)| [Python](./Round%201B/the-repeater.py)| _O(X * N)_ | _O(X * N)_ | Easy | | Math |
|B| [New Lottery Game](https://code.google.com/codejam/contest/2994486/dashboard#s=p1)| [Python](./Round%201B/new-lottery-game.py)| _O(log(max(A, B)))_ | _O(log(max(A, B)))_ | Medium | | Math, DP, Memoization |
|C| [The Bored Traveling Salesman](https://code.google.com/codejam/contest/2994486/dashboard#s=p2)| [Python](./Round%201B/the-bored-traveling-salesman.py)| _O(N^3)_ | _O(M + N)_ | Hard | | Greedy |

## Round 1C
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Part Elf](https://code.google.com/codejam/contest/3004486/dashboard#s=p0)| [Python](./Round%201C/part-elf.py)| _O(logQ)_ | _O(1)_ | Easy | | Math |
|B| [Reordering Train Cars](https://code.google.com/codejam/contest/3004486/dashboard#s=p1)| [Python](./Round%201C/reordering-train-cars.py)| _O(L)_ | _O(1)_ | Medium | | Math |
|C| [Enclosure](https://code.google.com/codejam/contest/3004486/dashboard#s=p2)| [Python](./Round%201C/enclosure.py)| _O(N^2 * M)_ | _O(1)_ | Hard | | Greedy, Math |

## Round 2
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Data Packing](https://code.google.com/codejam/contest/3014486/dashboard#s=p0)| | | | | | |
|B| [Up and Down](https://code.google.com/codejam/contest/3014486/dashboard#s=p1)| | | | | | |
|C| [Don't Break The Nile](https://code.google.com/codejam/contest/3014486/dashboard#s=p2)| | | | | | |
|D| [Trie Sharding](https://code.google.com/codejam/contest/3014486/dashboard#s=p3)| | | | | | |

## Round 3
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Magical, Marvelous Tour](https://code.google.com/codejam/contest/3024486/dashboard#s=p0)| | | | | | |
|B| [Last Hit](https://code.google.com/codejam/contest/3024486/dashboard#s=p1)| | | | | | |
|C| [Crime House](https://code.google.com/codejam/contest/3024486/dashboard#s=p2)| | | | | | |
|D| [Willow](https://code.google.com/codejam/contest/3024486/dashboard#s=p3)| | | | Very Hard | | |

## World Finals
You can relive the magic of the 2014 Code Jam World Finals by watching the [Live Stream Recording](https://www.youtube.com/watch?v=GYX3sn3Q_DQ) of the competition, problem explanations, interviews with Google and Code Jam engineers, and announcement of winners.

| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Checkboard Matrix](https://code.google.com/codejam/contest/7214486/dashboard#s=p0)| [Python](./World%20Finals/checkboard-matrix.py)| _O(N^2)_ | _O(N^2)_ | Medium | | |
|B| [Power Swapper](https://code.google.com/codejam/contest/7214486/dashboard#s=p1)| [Python](./World%20Finals/power-swapper.py)| _O(2^(N*2))_ | _O(2^N)_ | Medium | | Recursion |
|C| [Symmetric Trees](https://code.google.com/codejam/contest/7214486/dashboard#s=p2)| [Python](./World%20Finals/symmetric-trees.py)| _O(N^3 * logN)_ | _O(N^2)_ | Hard | | Recursion |
|D| [Paradox Sort](https://code.google.com/codejam/contest/7214486/dashboard#s=p3)| [Python](./World%20Finals/paradox-sort.py)| _O(N^2 * N!)_ | _O(N)_ | Hard | | DFS |
|E| [Allergy Testing](https://code.google.com/codejam/contest/7214486/dashboard#s=p4)| [Python](./World%20Finals/allergy-testing.py) [Python](./World%20Finals/allergy-testing2.py) | _O((logN)^3)_ | _O(1)_ | Hard | | Binary Search |
|F| [ARAM](https://code.google.com/codejam/contest/7214486/dashboard#s=p5)| [Python](./World%20Finals/aram.py)| _O(60 * N * R * G)_ | _O(1)_ | Very Hard | | Binary Search |
