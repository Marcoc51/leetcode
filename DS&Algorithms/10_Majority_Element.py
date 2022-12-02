class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = {}
        for num in nums:
            if num in res.keys():
                res[num] += 1
            else:
                res[num] = 1
        for key, value in res.items():
            if value > len(nums) / 2:
                return key
