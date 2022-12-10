class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            if nums[abs(num) - 1] > 0:
                nums[abs(num) - 1] = - nums[abs(num) - 1]
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]
        
