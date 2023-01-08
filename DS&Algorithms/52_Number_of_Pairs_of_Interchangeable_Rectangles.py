class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        res = 0
        div = defaultdict(int)
        for i, j in rectangles:
            div[i/j] += 1
        for value in div.values():
            res += value * (value - 1) // 2
        return res
