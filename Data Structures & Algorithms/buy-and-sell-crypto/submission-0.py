class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = 0
        
        while buy < len(prices):
            sell = buy + 1
            while sell < len(prices) and prices[sell] > prices[buy]:
                profit = max(profit, prices[sell] - prices[buy])
                sell += 1
            
            buy += 1

        return profit

        