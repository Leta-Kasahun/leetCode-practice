class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n=len(prices)
        buy=prices[0]
        profit=0
        for i in range(1,n):
            if prices[i]<buy:
                buy=prices[i]
            if prices[i]-buy>profit:
                profit=prices[i]-buy
        return profit            
