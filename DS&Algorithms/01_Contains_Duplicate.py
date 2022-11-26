from collections import Counter

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counts = Counter(nums)
        for num in list(counts.values()):
            if num > 1:
                return True
        return False
