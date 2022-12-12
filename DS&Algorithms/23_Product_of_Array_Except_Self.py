class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prev = [nums[0]]
        next = [nums[-1]]
        res = []
        for i in range(1, len(nums)):
            prev.append(prev[i - 1] * nums[i])
        for i in range(len(nums) - 2, -1, -1):
            next.insert(0, next[0] * nums[i])
        for i in range(len(nums)):
            if i == 0:
                res.append(next[i + 1])
            elif i - len(nums) == -1:
                res.append(prev[i - 1])
            else:
                res.append(prev[i - 1] * next[i + 1])
        return res
