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

        def get_neighbors(x, y):
            # left, right, above, below
            return ((x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y))

        m = len(board) - 1
        n = len(board[0]) - 1

        def is_inner_o(x, y):
            return x > 0 and x < m and y > 0 and y < n and board[x][y] == "O"

        def is_x(x, y):
            return board[x][y] == "X"

        for i in range(1, m):
            for j in range(1, n):
                if board[i][j] == "O":
                    queue = [(i, j)]
                    for x, y in queue:
                        matching_neighbors = 0
                        for neighbor in get_neighbors(x, y):
                            if is_inner_o(*neighbor):
                                queue.append(neighbor)
                                matching_neighbors += 1
                            elif is_x(*neighbor):
                                matching_neighbors += 1

                        if matching_neighbors == 4:
                            board[x][y] = "X"

        return board


print(
    Solution().solve(
        [
            ["X", "X", "X", "X"],
            ["X", "O", "O", "X"],
            ["X", "X", "O", "X"],
            ["X", "O", "X", "X"],
        ]
    )
)

# [["X","X","X","X"],
#  ["X","X","X","X"],
#  ["X","X","X","X"],
#  ["X","O","X","X"]]

print(Solution().solve([["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]]))
