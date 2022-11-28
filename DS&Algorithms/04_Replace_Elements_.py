class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [-1]
        j = -1
        for i in range(len(arr) - 1, 0, -1):
            if arr[i] >= res[j]:
                res.insert(0, arr[i])
            else:
                res.insert(0, res[j])
            j -= 1
        return res
