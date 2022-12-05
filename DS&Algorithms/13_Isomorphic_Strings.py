class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        for i in range(len(s)):
            if (s[i] in s_dict.keys() and t[i] != s_dict[s[i]]):
                return False
            elif (t[i] in t_dict.keys() and s[i] != t_dict[t[i]]):
                return False
            else:
                s_dict[s[i]] = t[i]
                t_dict[t[i]] = s[i]
        return True
