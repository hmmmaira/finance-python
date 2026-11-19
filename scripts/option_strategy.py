#getting the option strategy from the user 
option_strategy = input("enter the selected strategy (long_call,long_put, short_call, short_put): ").strip().lower()
valid_strategies = ["long_call","short_call","long_put","short_put"]
if option_strategy in valid_strategies:
#take the common input in all strategies
    strike_price = float(input("enter strike price: "))
    stock_price = float(input("enter stock price: "))
    premium = float(input("enter the option premium paid or received : "))

    #payoff and profit calculation
    if option_strategy == 'long_call' :
        payoff = max(0,(stock_price - strike_price))
        profit = payoff - premium
        breakeven = strike_price + premium 
        print(f"the payoff for the long call position: {payoff:.2f}, profit: {profit:.2f}, breakeven price: {breakeven:.2f}")
    elif option_strategy == 'short_call':
        payoff = -max(0,stock_price - strike_price)
        profit = payoff + premium
        breakeven = strike_price + premium
        print(f"the payoff for the short call position: {payoff:.2f}, profit: {profit:.2f}, breakeven price: {breakeven:.2f}")
    elif option_strategy == 'long_put':
        payoff = max(0, strike_price - stock_price)
        profit = payoff - premium
        breakeven = strike_price - premium 
        print(f"the payoff for the long put position {payoff:.2f}, profit: {profit:.2f}, breakeven price: {breakeven:.2f}")
    elif option_strategy == 'short_put':
        payoff = -max(0, strike_price - stock_price)
        profit = payoff + premium 
        breakeven = strike_price - premium 
        print(f"the payoff for the short put position: {payoff:.2f},profit: {profit:.2f}, breakeven price: {breakeven}")
else : 
    print('please select amongst the strategies provided')

