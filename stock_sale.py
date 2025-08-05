def stock_sale(prices):
    if len(prices)<2:
        return 0

    min_prices=prices[0]
    max_profit=0
    
    for i in range(1,len(prices)):
      current_price=prices[i]
      
      profit=current_price-min_prices
      
      if profit>max_profit:
        max_profit=profit

      if current_price<min_prices:
        min_prices=current_price
    
    return max_profit

if __name__=="__main__":
    prices=[7,1,5,3,6,4]
    print(stock_sale(prices))

        
    