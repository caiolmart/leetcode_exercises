from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return list()
        nums = sorted(nums)
        divisible = [
            nums, 
            [1 for i in range(len(nums))],
            [None for i in range(len(nums))]
        ]
        max_i = 0
        for i in range(1, len(nums)):
            n = divisible[0][i]
            for j in range(i - 1, -1, -1):
                if divisible[1][j] + 1 > divisible[1][i] and n % divisible[0][j] == 0:
                    divisible[1][i] = divisible[1][j] + 1
                    divisible[2][i] = j
                    if divisible[1][i] > divisible[1][max_i]:
                        max_i = i
        i = max_i
        max_set = [divisible[0][i]]
        while divisible[2][i] is not None:
            i = divisible[2][i]
            max_set.append(divisible[0][i])
        max_set.reverse()
        return max_set

if __name__ == "__main__":
    sol = Solution()
    print(sol.largestDivisibleSubset([1, 2, 3]))
    print(sol.largestDivisibleSubset([1, 2, 4, 8, 16]))