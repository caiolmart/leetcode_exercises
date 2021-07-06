from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n_papers = len(citations)
        min_ni = 0
        max_ni = n_papers
        while min_ni < max_ni:
            ni = min_ni + (max_ni - min_ni) // 2
            if citations[ni] >= n_papers - ni:
                max_ni = ni
            else:
                min_ni = ni + 1
        return n_papers - min_ni

if __name__ == "__main__":
    sol = Solution()
    print(sol.hIndex([0,1,3,5,6]))
    print(sol.hIndex([0,1,4,4,5,6]))