class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        for i in range(1, len(nums), 2):
            l = i - 1
            curr = nums[i]
            nums[i] = nums[l]
            nums[l] = curr
        return nums
        
