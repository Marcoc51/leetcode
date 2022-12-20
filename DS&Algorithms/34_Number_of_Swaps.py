class Solution:
    def minSwaps(self, s: str) -> int:
        closed = 0
        mx = 0
        res = 0
        for char in s:
            if char == ']':
                closed += 1
            else:
                closed -= 1
            mx = max(mx, closed)
        res = mx / 2
        return math.ceil(res)
