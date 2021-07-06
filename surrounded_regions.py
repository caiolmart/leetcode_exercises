from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) < 3 or len(board[0]) < 3:
            return
        aux_board = [[board[i][j] for j in range(len(board[0]))] for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = 'X'
        observed = set()
        def propagate(i, j):
            if (i, j) in observed:
                return
            if i < 0 or i >= len(aux_board) or j < 0 or j >= len(aux_board[0]):
                return
            observed.add((i, j))
            if aux_board[i][j] == 'O':
                board[i][j] = 'O'
                propagate(i - 1, j)
                propagate(i, j + 1)
                propagate(i + 1, j)
                propagate(i, j - 1)
        i = 0
        j = 0
        observed.add((i, j))
        board[i][j] = aux_board[i][j]
        j += 1
        while j < len(aux_board[0]) - 1:
            board[i][j] = aux_board[i][j]
            observed.add((i, j))
            if aux_board[i][j] == 'O':
                propagate(i + 1, j)
            j += 1
        observed.add((i, j))
        board[i][j] = aux_board[i][j]
        i += 1
        while i < len(aux_board) - 1:
            board[i][j] = aux_board[i][j]
            observed.add((i, j))
            if aux_board[i][j] == 'O':
                propagate(i, j - 1)
            i += 1
        observed.add((i, j))
        board[i][j] = aux_board[i][j]
        j -= 1
        while j > 0:
            board[i][j] = aux_board[i][j]
            observed.add((i, j))
            if aux_board[i][j] == 'O':
                propagate(i - 1, j)
            j -= 1
        observed.add((i, j))
        board[i][j] = aux_board[i][j]
        i -= 1
        while i > 0:
            board[i][j] = aux_board[i][j]
            observed.add((i, j))
            if aux_board[i][j] == 'O':
                propagate(i, j + 1)
            i -= 1
        return

if __name__ == "__main__":
    sol = Solution()
    board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    sol.solve(board)
    board = [["O","O","O"],["O","O","O"],["O","O","O"]]
    sol.solve(board)
    print(board)