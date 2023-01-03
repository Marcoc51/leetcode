class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        ned = len(needle)
        for i in range(len(haystack) - ned + 1):
            if haystack[i: i + ned] == needle:
                return i
        return -1
