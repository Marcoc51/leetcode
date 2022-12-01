class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        j = 0
        for char in strs[0]:
            for i in range(1, len(strs)):
                try:
                    if char != strs[i][j]:
                        return res
                except:
                    return res
            j += 1
            res += char
        else:
            return res
