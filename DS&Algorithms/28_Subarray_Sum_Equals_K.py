class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum = 0
        res = 0
        sub = {0: 1}
        for num in nums:
            sum += num
            if sum - k in sub.keys():
                res += sub[sum - k]
            if sum in sub.keys():
                sub[sum] += 1
            else:
                sub[sum] = 1
        return res
        
