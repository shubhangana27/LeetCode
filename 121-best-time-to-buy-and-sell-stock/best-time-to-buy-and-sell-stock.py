class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_p=float('inf')
        sell_p=0
        profit=0
        for i in prices:
            if i<buy_p:
                buy_p=i
            elif i-buy_p>profit:
                sell_p=max(sell_p,i)
                profit=i-buy_p
        return profit
