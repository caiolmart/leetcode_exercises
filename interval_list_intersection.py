from typing import List


class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        a_idx = 0
        b_idx = 0
        a_len = len(A)
        b_len = len(B)
        ans = list()
        while a_idx < a_len and b_idx < b_len:
            min_inter = max(A[a_idx][0], B[b_idx][0])
            max_inter = min(A[a_idx][1], B[b_idx][1])
            if max_inter >= min_inter:
                ans.append([min_inter, max_inter])
            
            if A[a_idx][1] > B[b_idx][1]:
                b_idx += 1
            else:
                a_idx += 1
        return ans

if __name__ == "__main__":
    sol = Solution()
    A = [[0,2],[5,10],[13,23],[24,25]]
    B = [[1,5],[8,12],[15,24],[25,26]]
    print(sol.intervalIntersection(A, B))
