from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            grid[i] = [0] + grid[i] + [0]
        grid.insert(m, [0] * (n + 2))
        grid.insert(0, [0] * (n + 2))
        ans = 0
        for i in range(m + 2):
            for j in range(n + 2):
                if grid[i][j] == 0:
                    if i > 0:
                        ans += grid[i - 1][j]
                    if i < m:
                        ans += grid[i + 1][j]
                    if j > 0:
                        ans += grid[i][j - 1]
                    if j < n:
                        ans += grid[i][j + 1]
        return ans

if __name__ == "__main__":
    sol = Solution()
    grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
    print(sol.islandPerimeter(grid))