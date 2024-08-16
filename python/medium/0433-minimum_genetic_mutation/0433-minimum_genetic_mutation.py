"""
https://leetcode.com/problems/minimum-genetic-mutation/

A gene string can be represented by an 8-character long string, with
choices from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene string startGene
to a gene string endGene where one mutation is defined as one single
character changed in the gene string.

For example, "AACCGGTT" --> "AACCGGTA" is one mutation. There is also
a gene bank bank that records all the valid gene mutations. A gene
must be in bank to make it a valid gene string.

Given the two gene strings startGene and endGene and the gene bank
bank, return the minimum number of mutations needed to mutate from
startGene to endGene. If there is no such a mutation, return -1.

Note that the starting point is assumed to be valid, so it might not
be included in the bank.


Example 1:
Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
Output: 1

Example 2:
Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
Output: 2
"""

from typing import List
from collections import defaultdict


class Graph:
    def __init__(self):
        self.edges = defaultdict(set)

    def add_edge(self, from_node, to_node):
        self.edges[from_node].add(to_node)

    def find_paths(self, start, end):
        paths = []
        queue = [[start]]
        for p in queue:
            for node in self.edges[p[-1]]:
                if node in p:
                    continue  # we're looping
                else:
                    path = p.copy()
                    path.append(node)
                    if node == end:
                        paths.append(path)
                    else:
                        queue.append(path)
        return paths


class Solution:
    def __init__(self):
        self.graph = Graph()

    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        def _valid_mutation(g0, g1):
            variations = 0
            for i in range(len(g0)):
                if g0[i] != g1[i]:
                    variations += 1
                    if variations > 1:
                        return False
            return True

        if startGene not in bank:
            bank.append(startGene)

        n = len(bank)
        for i in range(n):
            for j in range(n):
                if i != j and _valid_mutation(bank[i], bank[j]):
                    self.graph.add_edge(bank[i], bank[j])

        paths = self.graph.find_paths(startGene, endGene)
        if paths:
            return len(min(paths, key=len)) - 1
        else:
            return -1


# # Example 2:
# # Input: startGene = "AACCGGTT", endGene = "AAACGGTA",
# # bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
# # Output: 2
# print(
#     Solution().minMutation("AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"])
# )
# # 2

# print(
#     Solution().minMutation(
#         "AAAACCCC",
#         "CCCCCCCC",
#         [
#             "AAAACCCA",
#             "AAACCCCA",
#             "AACCCCCA",
#             "AACCCCCC",
#             "ACCCCCCC",
#             "CCCCCCCC",
#             "AAACCCCC",
#             "AACCCCCC",
#         ],
#     )
# )

# # 4
