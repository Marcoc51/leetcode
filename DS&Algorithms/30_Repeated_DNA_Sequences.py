class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res = {}
        ans = []
        if len(s) < 10:
            return ans
        for i in range(len(s) - 9):
            p = s[i: i + 10]
            if p in res.keys():
                res[p] += 1
            else:
                res[p] = 1
        mx = max(res.values())
        if mx < 2:
            return ans
        sort_res = dict(sorted(res.items(), key=lambda x: x[1], reverse=True))
        for key, value in sort_res.items():
            if value != mx:
                break
            ans.append(key)
        return ans
