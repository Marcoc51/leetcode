class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums1)):
            j = nums2.index(nums1[i])
            if nums2[j] == nums2[-1]:
                ans.append(-1)
            else:
                for k in range(j + 1, len(nums2)):
                    if nums2[k] > nums2[j]:
                        ans.append(nums2[k])
                        break
                else:
                    ans.append(-1)
        return ans
