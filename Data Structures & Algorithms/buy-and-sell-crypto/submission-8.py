class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        smallest = prices[0]

        for p in prices:
            if((p - smallest) > profit):
                profit = p - smallest
            if(p < smallest):
                smallest = p
                
        return profit
            