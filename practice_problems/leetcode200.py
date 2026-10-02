"""
Problem https://leetcode.com/problems/number-of-islands/description/ :

Post Completion Reflections:
    
200. Number of Islands
Medium
Topics
premium lock icon
Companies
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

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
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.

"""

# =========================== Your Solution Below ========================== #

# from gemini
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        # Edge case: empty grid
        if not grid:
            return 0
            
        island_count = 0
        rows = len(grid)
        cols = len(grid[0])
        
        # Helper function to "sink" the connected land
        def explore_and_sink(r, c):
            # Base cases to stop recursion:
            # 1. We went out of bounds
            # 2. We hit water ("0")
            if (r < 0 or r >= rows or 
                c < 0 or c >= cols or 
                grid[r][c] == "0"):
                return
            
            # Mark the current cell as visited by turning it to water
            grid[r][c] = "0"
            
            # Recursively explore all 4 adjacent directions
            explore_and_sink(r + 1, c) # Down
            explore_and_sink(r - 1, c) # Up
            explore_and_sink(r, c + 1) # Right
            explore_and_sink(r, c - 1) # Left

        # Main loop: scan every cell in the grid
        for i in range(rows):
            for j in range(cols):
                # When we find unvisited land...
                if grid[i][j] == "1":
                    island_count += 1        # 1. Count it!
                    explore_and_sink(i, j)   # 2. Sink the whole island so we don't count it again
                    
        return island_count


# =========================== Your Solution Above ========================== #

if __name__ == "__main__":
    sol = Solution()
    assert sol.numIslands([["1", "0"], ["0", "1"]]) == 2
