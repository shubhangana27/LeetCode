class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_p=float('inf')
        profit=0
        for i in prices:
            if i<buy_p:
                buy_p=i
            elif i-buy_p>profit:
                profit=i-buy_p
        return profit
