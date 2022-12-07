class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        k_dict = {}
        if len(nums) == k:
            return nums
        for i in range(len(nums)):
            if nums[i] in k_dict.keys():
                k_dict[nums[i]] += 1
            else:
                k_dict[nums[i]] = 1
        sorted_dict = dict(sorted(k_dict.items(), key=lambda item: item[1], reverse=True))
        return list(sorted_dict.keys())[:k]
