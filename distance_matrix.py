from typing import List


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        distances = [[None for j in range(n)] for i in range(m)]
        border = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    border.append((i, j, 0))
        level = 0
        while border:
            pos = border.pop(0)
            distance[pos[0]][pos[1]] = pos[3]
            if pos[0] - 1 >= 0 and



if __name__ == "__main__":
    sol = Solution()
    sol.updateMatrix([[1,1,0,0,1,0,0,1,1,0],[1,0,0,1,0,1,1,1,1,1],[1,1,1,0,0,1,1,1,1,0],[0,1,1,1,0,1,1,1,1,1],[0,0,1,1,1,1,1,1,1,0],[1,1,1,1,1,1,0,1,1,1],[0,1,1,1,1,1,1,0,0,1],[1,1,1,1,1,0,0,1,1,1],[0,1,0,1,1,0,1,1,1,1],[1,1,1,0,1,0,1,1,1,1]])