import numpy as np 
import matplotlib.pyplot as plt

def calculate_option(strategy,strike_price,stock_range,premium):
    if strategy == 'long_call':
        payoff = np.maximum(0,stock_range - strike_price)
        profit = payoff - premium
        breakeven = strike_price + premium
        return payoff,profit,breakeven
    elif strategy == 'short_call':
        payoff = -np.maximum(0,stock_range - strike_price)
        profit = payoff + premium
        breakeven = strike_price + premium 
        return payoff, profit,breakeven
    elif strategy == 'long_put' :
        payoff = np.maximum(0, strike_price - stock_range)
        profit = payoff - premium
        breakeven = strike_price - premium
        return payoff,profit,breakeven
    elif strategy == 'short_put' :
        payoff = -np.maximum(0,strike_price - stock_range)
        profit = payoff + premium 
        breakeven = strike_price - premium
        return payoff, profit, breakeven

option_strategy = input("enter the selected strategy (long_call,long_put, short_call, short_put): ").strip().lower()
valid_strategies = ["long_call","short_call","long_put","short_put"]
if option_strategy in valid_strategies:
#take the common input in all strategies
    print("please enter positive values for the inputs")
    strike_price = float(input("enter strike price: "))
    lower_stock = float(input('enter the lower bound for the stock price: '))
    upper_stock = float(input('enter the upper bound for the stock price '))
    interval = float(input('enter the price intervals to plot: '))
    stock_range = np.arange(lower_stock,upper_stock + interval,interval)
    premium = float(input("enter the option premium paid or received : "))
# call the function to calculate payoff, profit and breakeven
    payoff,profit,breakeven = calculate_option(
    option_strategy,strike_price,stock_range,premium)
    print('\n ---OPTIONS ANALYSIS---')
    print('stock range: ', stock_range)
    print("profit: ",profit)
    print('payoff: ',payoff)
    print('breakeven: ', breakeven)
else :
    print("please enter an available option")

#plotting the chart
plt.plot(stock_range,payoff, label = 'payoff')
plt.plot(stock_range,profit, label = 'profit')
plt.xlabel('stock price range at expiration')
plt.ylabel('payoff/profit')
plt.title('option strategy analysis')
plt.legend()
plt.show()

