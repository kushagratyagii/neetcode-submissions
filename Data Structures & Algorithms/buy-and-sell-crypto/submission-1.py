class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buying_date = 0
        selling_date = 1
        
        while selling_date <= len(prices)-1:
            if prices[selling_date] > prices[buying_date]:
                profit = max(profit,prices[selling_date]- prices[buying_date])
            else:
                buying_date = selling_date
            selling_date += 1

        return profit