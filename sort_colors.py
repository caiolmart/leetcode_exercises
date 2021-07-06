from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_zero = -1
        first_two = len(nums)
        i = 0
        while i < first_two:
            if nums[i] == 0:
                last_zero += 1
                nums[i], nums[last_zero] = nums[last_zero], nums[i]
            while nums[i] == 2 and i < first_two:
                first_two -= 1
                nums[i], nums[first_two] = nums[first_two], nums[i]
                if nums[i] == 0:
                    last_zero += 1
                    nums[i], nums[last_zero] = nums[last_zero], nums[i]
            i += 1

if __name__ == "__main__":
    sol = Solution()
    print(sol.sortColors([2,0,2,1,1,0]))
    print(sol.sortColors([2,1,2]))
    print(sol.sortColors([2,2,2]))
    print(sol.sortColors([1,1,1]))
    print(sol.sortColors([0,0,0]))
