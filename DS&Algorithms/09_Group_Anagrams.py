class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for str in strs:
            sorted_str = ''.join(sorted(str))
            res[sorted_str].append(str)
        return list(res.values())
