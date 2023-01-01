class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        mod = pow(10, 9) + 7
        res = 0
        power = [pow(2, i, mod) for i in range(len(nums))]
        l = 0
        r = len(nums) - 1
        while l <= r:
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                res += power[r - l]
                l += 1
        return res % mod
