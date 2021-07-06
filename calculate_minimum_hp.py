from typing import List

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])
        def get_diagonal(k):
            this_m = m - 1
            this_n = n - k - 1
            diagonal = list()
            while this_n < n:
                if this_m >= 0 and this_n >= 0:
                    diagonal.append([this_m, this_n])
                this_m -= 1
                this_n += 1
            return diagonal
        min_hp = [[float('inf') for j in range(n + 1)] for i in range(m + 1)]
        min_hp[m - 1][n - 1] = -dungeon[m - 1][n - 1] + 1
        for i in range(1, m + n):
            diagonal = get_diagonal(i)
            for p in diagonal:
                min_hp[p[0]][p[1]] = -dungeon[p[0]][p[1]]
                min_hp[p[0]][p[1]] = max(min_hp[p[0]][p[1]] + 1,
                                         min_hp[p[0]][p[1]] + min(min_hp[p[0] + 1][p[1]], 
                                                                  min_hp[p[0]][p[1] + 1]))
        return max(1, min_hp[0][0])

if __name__ == "__main__":
    sol = Solution()
    dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
    print(sol.calculateMinimumHP(dungeon))
    dungeon = [[-3,5]]
    print(sol.calculateMinimumHP(dungeon))