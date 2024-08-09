"""
https://leetcode.com/problems/number-of-islands/

Given an m x n 2D binary grid grid which represents a map of '1's
(land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent
lands horizontally or vertically. You may assume all four edges of the
grid are all surrounded by water.


Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""

from typing import List
from collections import defaultdict


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(set)

    def add_node(self, node_id):
        self.nodes.add(node_id)

    def add_edge(self, from_node, to_node):
        self.edges[from_node].add(to_node)
        self.edges[to_node].add(from_node)

    def reachable_from(self, node):
        visited = set([node])
        queue = [node]
        for node in queue:
            for n in self.edges[node]:
                if n in visited:
                    continue
                else:
                    visited.add(n)
                    queue.append(n)
        return visited

    def get_nodes(self):
        return self.nodes.copy()


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def cell_id(i, j, n):
            return (i * (n + 1)) + j

        graph = Graph()
        m = len(grid) - 1
        n = len(grid[0]) - 1
        i = 0
        while i <= m:
            j = 0
            while j <= n:
                # Is this cell land?
                if grid[i][j] == "1":
                    node_id = cell_id(i, j, n)
                    graph.add_node(node_id)

                    # Does it have land to the right?
                    if j < n and grid[i][j + 1] == "1":
                        graph.add_edge(node_id, cell_id(i, j + 1, n))

                    # Does it have land bellow?
                    if i < m and grid[i + 1][j] == "1":
                        graph.add_edge(node_id, cell_id(i + 1, j, n))
                j += 1
            i += 1

        nodes = graph.get_nodes()
        cnt = 0
        while nodes:
            cnt += 1
            node = nodes.pop()
            reachable = graph.reachable_from(node)
            nodes = nodes - reachable
        return cnt


# g = Solution().numIslands(
print(
    Solution().numIslands(
        [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
    )
)

# print(g.nodes)
# # {0, 1, 5, 6, 12, 18, 19}

# # For debugging - this only uses one directed edge, outbound from
# # low-order nodes.
# print(g.edges)
# # {0: {1, 5},
# #  1: {6},
# #  5: {6},
# #  18: {19}})

# # Full edge set
# # {0: {1, 5},
# #  1: {0, 6},
# #  5: {0, 6},
# #  6: {1, 5},
# #  18: {19},
# #  19: {18}}

# print(g.reachable_from(19))
