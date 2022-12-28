class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            start = i + 1
            end = len(nums) - 1
            while start < end:
                sm = nums[i] + nums[start] + nums[end]
                if sm == 0:
                    res.append([nums[i], nums[start], nums[end]])
                    Vstart = nums[start]
                    Vend = nums[end]
                    while start < end and nums[start] == Vstart:
                        start += 1
                    while start < end and nums[end] == Vend:
                        end -= 1
                elif sm < 0:
                    start += 1
                else:
                    end -= 1
        return res
