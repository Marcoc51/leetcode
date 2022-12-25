class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        while l < len(nums) - 1:
            if nums[l] == nums[l + 1]:
                nums.pop(l)
            else:
                l += 1
        return len(nums)
