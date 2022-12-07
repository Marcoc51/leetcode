class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p_dict = dict()
        s_dict = dict()
        s_list = s.split(' ')
        if len(pattern) != len(s_list):
            return False
        for i in range(len(pattern)):
            if pattern[i] in p_dict.keys() and p_dict[pattern[i]] != s_list[i]:
                return False
            p_dict[pattern[i]] = s_list[i]
        for i in range(len(s_list)):
            if s_list[i] in s_dict.keys() and s_dict[s_list[i]] != pattern[i]:
                return False
            s_dict[s_list[i]] = pattern[i]
        return True
