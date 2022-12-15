class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mx = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                mx += prices[i + 1] - prices[i]
        return mx
        
