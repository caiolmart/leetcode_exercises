from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        max_len = [0] * len(nums)
        for i in range(1, len(nums)):
            if i - max_len[i - 1] - 1 >= 0 and nums[i] + nums[i - max_len[i - 1] - 1] == 1:
                max_len[i] = max_len[i - 1] + 2 + max_len[i - max_len[i - 1] - 2]
            else:
                j = i - max_len[i - 1]
                n_zeros = max_len[i - 1] // 2 + ((nums[i] == 0) * 1)
                n_ones = max_len[i - 1] // 2 + ((nums[i] == 1) * 1)
                while n_zeros != n_ones:
                    n_zeros -= (nums[j] == 0) * 1
                    n_ones -= (nums[j] == 1) * 1
                    j += 1
                max_len[i] = n_zeros + n_ones
        return max(max_len)

if __name__ == "__main__":
    sol = Solution()
    #print(sol.findMaxLength([0, 1, 0]))
    print(sol.findMaxLength([0,1,0,1]))
    #print(sol.findMaxLength([0, 1, 0, 0, 1, 1, 0]))