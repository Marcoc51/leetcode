class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        right = sum(nums[1:])
        left = 0
        for i in range(len(nums)):
            if right == left:
                return i
            else:
                try:
                    right -= nums[i + 1]
                    left += nums[i]
                except:
                    return -1
