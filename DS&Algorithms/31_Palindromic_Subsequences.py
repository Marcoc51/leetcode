class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        from collections import defaultdict

        chars = defaultdict(list)
        res = set()
        for i in range(len(s)):
            chars[s[i]].append(i)
        values = list(chars.values())
        for i in range(len(values)):
            if len(values[i]) > 1:
                start = values[i][0] + 1
                end = values[i][-1]
                for j in range(start, end):
                    res.add(s[start] + s[j] + s[end])
        return len(res)
        
