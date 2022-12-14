class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mx = 0
        s = set(nums)
        for i in range(len(nums)):
            if nums[i] - 1 not in s:
                l = 1
                while nums[i] + l in s:
                    l += 1
                mx = max(mx, l)
        return mx
