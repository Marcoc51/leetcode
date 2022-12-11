class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon = ['b', 'a', 'l', 'o', 'n']
        res = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
        for char in text:
            if char in balloon:
                res[char] += 1
        res['l'] //= 2
        res['o'] //= 2
        return min(res.values())
