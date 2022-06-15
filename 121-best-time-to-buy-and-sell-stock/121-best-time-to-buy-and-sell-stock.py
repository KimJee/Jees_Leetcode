
class Solution:
    def brute_force(self, prices: List[int]) -> int:
        result = 0
        
        """
            Brute force approach
            
            * (1) Buy date must be before the sell date
            * (2) The maximum amount of profit must be achived
        
        """
        for buy_date, buy_price in enumerate(prices):
            for sell_date, sell_price in enumerate(prices):
                if (buy_date < sell_date):
                    profit = sell_price - buy_price
                    if (profit > result):
                        result = profit
        return result
    
    def better_solution(self, prices: List[int]) -> int:
        """
            The key insight is... 
            when you're going through each day, you only care about the lowest price that you've seen so far.
            And then you determine profit.. if it is over the current_max replace it and if not keep going
        """
        
        max_profit = 0
        lowest_buy_price = prices[0]
        
        for index in range(1, len(prices), 1):
            selling_price = prices[index]
            profit = selling_price - lowest_buy_price
            if (profit > max_profit):
                max_profit = profit
            if (selling_price < lowest_buy_price):
                lowest_buy_price = selling_price
        
        return max_profit
        
    def maxProfit(self, prices: List[int]) -> int:
        return self.better_solution(prices)
        