class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(len(nums1)):
            if nums1[i] == 0 and len(nums2) != 0:
                nums1[i] = nums2.pop()
        nums1.sort()
