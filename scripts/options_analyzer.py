
def calculate_option(strategy,strike_price,stock_price,premium):
    if strategy == 'long_call':
        payoff = max(0,stock_price - strike_price)
        profit = payoff - premium
        breakeven = strike_price + premium
        return payoff,profit,breakeven
    elif strategy == 'short_call':
        payoff = -max(0,stock_price - strike_price)
        profit = payoff + premium
        breakeven = strike_price + premium 
        return payoff, profit,breakeven
    elif strategy == 'long_put' :
        payoff = max(0, strike_price - stock_price)
        profit = payoff - premium
        breakeven = strike_price - premium
        return payoff,profit,breakeven
    elif strategy == 'short_put' :
        payoff = -max(0,strike_price - stock_price)
        profit = payoff + premium 
        breakeven = strike_price - premium
        return payoff, profit, breakeven

option_strategy = input("enter the selected strategy (long_call,long_put, short_call, short_put): ").strip().lower()
valid_strategies = ["long_call","short_call","long_put","short_put"]
if option_strategy in valid_strategies:
#take the common input in all strategies
    print("please enter positive values for the inputs")
    strike_price = float(input("enter strike price: "))
    stock_price = float(input("enter stock price: "))
    premium = float(input("enter the option premium paid or received : "))
# call the function to calculate payoff, profit and breakeven
    payoff,profit,breakeven = calculate_option(
    option_strategy,strike_price,stock_price,premium)
    print(f'payoff: {payoff:.2f}, profit: {profit:.2f}, breakeven: {breakeven:.2f}')
else :
    print("please enter an available option")