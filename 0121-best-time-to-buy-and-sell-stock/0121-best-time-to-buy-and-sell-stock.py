class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        buy_index = 0
        buy_price = prices[0] # Assuming you buy the first day
        for i in range(1, len(prices), 1):
            sell_index = i
            sell_price = prices[i]
            if (buy_index < sell_index):
                profit = sell_price - buy_price
                max_profit = max(profit, max_profit)            
            if (sell_price < buy_price):
                buy_price = sell_price
                buy_index = sell_index
            # print("Buy Index:", buy_index, " Buy Price:", buy_price, " Sell Index:", sell_index, " Sell Price: ", sell_price, " Profit:", profit, max_profit)
        return max_profit
            
            
            


            