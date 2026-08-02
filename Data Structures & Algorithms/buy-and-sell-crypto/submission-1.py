class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lp,rp = 0,1
        profit = 0

        while (rp <= (len(prices) - 1)) and (lp <= rp):
            if(prices[rp] > prices[lp]):
                profit = max(prices[rp] - prices[lp], profit)
                rp += 1
            else:
                lp = rp
            
            if lp == rp:
                rp += 1
        
        return profit