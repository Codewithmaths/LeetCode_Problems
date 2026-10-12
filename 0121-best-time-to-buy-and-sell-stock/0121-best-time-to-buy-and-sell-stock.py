class Solution:
    def maxProfit(self, prices: list[int]) -> int:
            if len(prices)<=1:
                return 0
            l = min(prices)
            ind = prices.index(l)                  
            if len(prices[ind:]) <= 1:
                max_profit = 0
                return max(max_profit, self.maxProfit(prices[:ind]))          
            else:
                max_profit = max(prices[ind:]) - l                              
                if len(prices[:ind]) <= 1:
                    return max_profit
                else:
                    return max(max_profit, self.maxProfit(prices[:ind]))
            

        
                

            

            
        