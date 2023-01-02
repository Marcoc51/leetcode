class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                l = j + 1
                r = len(nums) - 1
                while l < r:
                    sm = nums[i] + nums[j] + nums[l] + nums[r]
                    if sm == target:
                        res.add((nums[i], nums[j], nums[l], nums[r]))
                        l_value = nums[l]
                        r_value = nums[r]
                        while l < r and nums[l] == l_value:
                            l += 1
                        while l < r and nums[r] == r_value:
                            r -= 1
                    elif sm < target:
                        l += 1
                    else:
                        r -= 1
        return res
