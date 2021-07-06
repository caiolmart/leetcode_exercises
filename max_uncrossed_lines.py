from typing import List

class Solution:
    dp = None
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        if len(A) == 0 or len(B) == 0:
            return 0
        dp = [[None for j in range(len(B))] for i in range(len(A))]
        
        def sub_max_lines(A, B):
            len_a = len(A)
            len_b = len(B)
            max_a = len(dp)
            max_b = len(dp[0])
            if len_a == 0 or len_b == 0:
                return 0
            if dp[max_a - len_a][max_b - len_b] is not None:
                return dp[max_a - len_a][max_b - len_b]
            max_cuts = 0
            for i in range(len_a):
                if A[i] in B:
                    max_cuts = max(max_cuts, 1 + sub_max_lines(A[i + 1:], B[B.index(A[i]) + 1:]))
            dp[max_a - len_a][max_b - len_b] = max_cuts
            return max_cuts
        
        return sub_max_lines(A, B)

if __name__ == "__main__":
    sol = Solution()
    A = [2,5,1,2,5]
    B = [10,5,2,1,5,2]
    print(sol.maxUncrossedLines(A, B))