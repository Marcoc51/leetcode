class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        if len(p) > len(s): return res
        p_dict = defaultdict(int)
        s_dict = defaultdict(int)
        for char in p: p_dict[char] += 1
        start = 0
        for i in range(len(s)):
            s_dict[s[i]] += 1
            if i >= len(p):
                s_dict[s[start]] -= 1
                if s_dict[s[start]] == 0:
                    del s_dict[s[start]]
                start += 1
            if s_dict == p_dict:
                res.append(start)
        return res
