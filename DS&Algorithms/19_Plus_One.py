class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s_list = [str(i) for i in digits]
        s = ''.join(s_list)
        num = int(s)
        num += 1
        res = [int(i) for i in str(num)]
        return res
