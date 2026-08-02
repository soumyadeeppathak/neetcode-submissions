class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lp,rp = 0,1
        profit = 0
        length = len(prices) - 1

        while (rp <= length):
            if(prices[rp] > prices[lp]):
                profit = max(prices[rp] - prices[lp], profit)
                rp += 1
            else:
                lp = rp
                rp += 1
        
        return profit