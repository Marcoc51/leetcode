class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        nums.sort(reverse=True)
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                num1 = int(nums[i] + nums[j])
                num2 = int(nums[j] + nums[i])
                if num2 > num1:
                    curr = nums[i]
                    nums[i] = nums[j]
                    nums[j] = curr
        if nums[0] == "0":
            return "0"
        res = ''.join(nums)
        return res
