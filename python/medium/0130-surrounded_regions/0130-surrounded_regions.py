"""
https://leetcode.com/problems/surrounded-regions/

You are given an m x n matrix board containing letters 'X' and 'O',
capture regions that are surrounded:

* Connect: A cell is connected to adjacent cells horizontally or vertically.
* Region: To form a region connect every 'O' cell.
* Surround: The region is surrounded with 'X' cells if you can connect
the region with 'X' cells and none of the region cells are on the edge
of the board.

A surrounded region is captured by replacing all 'O's with 'X's in the
input matrix board.

Example 1:

Input: board =
[["X","X","X","X"],
 ["X","O","O","X"],
 ["X","X","O","X"],
 ["X","O","X","X"]]

Output:
[["X","X","X","X"],
 ["X","X","X","X"],
 ["X","X","X","X"],
 ["X","O","X","X"]]

Explanation:
In the above diagram, the bottom region is not captured because it is
on the edge of the board and cannot be surrounded.


Example 2:

Input: board = [["X"]]

Output: [["X"]]

"""

from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board) - 1
        n = len(board[0]) - 1

        def get_o_neighbors(x, y):
            neighbors = []
            # Check left
            if y > 0 and board[x][y - 1] == "O":
                neighbors.append((x, y - 1))

            # Check above
            if x > 0 and board[x - 1][y] == "O":
                neighbors.append((x - 1, y))

            # Check right
            if y < n and board[x][y + 1] == "O":
                neighbors.append((x, y + 1))

            # Check below
            if x < m and board[x + 1][y] == "O":
                neighbors.append((x + 1, y))

            return neighbors

        def mark_cells(x, y):
            if board[x][y] == "O":
                queue = [(x, y)]
                while queue:
                    x, y = queue.pop()
                    board[x][y] = "M"
                    for neighbor in get_o_neighbors(x, y):
                        queue.append(neighbor)

        # Mark Os to save, from top or bottom row
        for x in (0, m):
            for y in range(0, n + 1):
                mark_cells(x, y)

        # Mark Os to save, from left or right edge
        for y in (0, n):
            for x in range(0, m + 1):
                mark_cells(x, y)

        # Final pass to flip unmarked Os to Xs, and then revert marked
        # ("M") Os to Os.
        for x in range(m + 1):
            for y in range(n + 1):
                if board[x][y] == "O":
                    board[x][y] = "X"
                elif board[x][y] == "M":
                    board[x][y] = "O"

        return board


# print(
#     Solution().solve(
#         [
#             ["X", "X", "X", "X"],
#             ["X", "O", "O", "X"],
#             ["X", "X", "O", "X"],
#             ["X", "O", "X", "X"],
#         ]
#     )
# )

# [["X","X","X","X"],
#  ["X","X","X","X"],
#  ["X","X","X","X"],
#  ["X","O","X","X"]]

# print(Solution().solve([["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]]))

# # [["O", "O", "O"],
# #  ["O", "O", "O"],
# #  ["O", "O", "O"]]


print(
    Solution().solve(
        [
            ["O", "O", "O", "O"],
            ["O", "O", "O", "O"],
            ["O", "O", "O", "O"],
            ["O", "O", "O", "O"],
        ]
    )
)
