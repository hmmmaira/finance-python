strike_price = float(input("enter strike price: "))
stock_price = float(input("enter stock price: "))
premium = float(input("enter the call premium paid: "))
payoff = max(0,(stock_price - strike_price))
profit = payoff - premium
print(f"the payoff for the long call position is {payoff:.2f} and the profit generate is {profit:.2f}")