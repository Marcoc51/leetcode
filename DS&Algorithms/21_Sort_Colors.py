class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                curr = nums[i]
                if nums[i] > nums[j]:
                    nums[i] = nums[j]
                    nums[j] = curr
