class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=0
        sell=1
        new_profit = 0
        while buy < len(prices) and sell<len(prices):
            if prices[sell]>prices[buy]:
                new_profit=max(new_profit,prices[sell]-prices[buy])
                sell+=1
            else:
                buy=sell
                sell+=1
        return new_profit
            

        