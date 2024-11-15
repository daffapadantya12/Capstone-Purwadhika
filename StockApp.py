import random

watchlist = [
    "AAPL",
    "MSFT",
    "AMZN",
    "NVDA",
    "TSLA"
    ]

portfolio = {
    'AAPL': 5,    
    'GOOGL': 7,  
    'MSFT': 2,    
    'AMZN': 3,   
    }  # key: stock_symbol, value: quantity_owned

available_stocks = {
    'AAPL': 150.00,    # Apple Inc.
    'GOOGL': 179.00,  # Alphabet Inc. (Google)
    'MSFT': 300.00,    # Microsoft Corporation
    'AMZN': 350.00,   # Amazon.com, Inc.
    'META': 350.00,    # Meta Platforms, Inc. (Facebook)
    'TSLA': 700.00,    # Tesla, Inc.
    'NFLX': 550.00,    # Netflix, Inc.
    'NVDA': 220.00,    # NVIDIA Corporation
    'JPM': 160.00,     # JPMorgan Chase & Co.
    'BAC': 40.00,      # Bank of America Corporation
    'DIS': 180.00,     # The Walt Disney Company
    'V': 230.00,       # Visa Inc.
    'ADBE': 500.00,    # Adobe Inc.
    'PYPL': 250.00,    # PayPal Holdings, Inc.
    'INTC': 55.00,     # Intel Corporation
    'CSCO': 50.00,     # Cisco Systems, Inc.
    'PEP': 150.00,     # PepsiCo, Inc.
    'KO': 55.00,       # The Coca-Cola Company
    'IBM': 140.00,     # International Business Machines Corporation
    'ORCL': 85.00      # Oracle Corporation      
}

price_flactuation = {}  # key: stock_symbol, value: current_price

def initialize_prices(): #set the stock price
    for symbol, price in available_stocks.items():
        price_flactuation[symbol] = price

def simulate_price_change(symbol): #simulate the price change
    current_price = price_flactuation.get(symbol, available_stocks[symbol])
    # Simulate price change by a random percentage between -5% and +5%
    percentage_change = random.uniform(-0.05, 0.05)
    new_price = current_price * (1 + percentage_change)
    # Ensure the price doesn't drop below 1, if so...stay at 1
    if new_price < 1:
        new_price = 1.00
    price_flactuation[symbol] = round(new_price, 2)
    return price_flactuation[symbol]

def add_stock(symbol): #Add a stock symbol to the watchlist
  

    symbol = symbol.upper()
    if symbol not in available_stocks:
        print(f"{symbol} is not available")
        return
    if symbol not in watchlist:
        watchlist.append(symbol)
        print(f"{symbol} has been added to your watchlist.")
    else:
        print(f"{symbol} is already in your watchlist.")

def get_stock_data(symbol): # Simulate a price change each time data is requested
    price = simulate_price_change(symbol)
    return {
        'symbol': symbol,
        'price': price
    }

def update_stock(old_symbol, new_symbol): #Replace a stock symbol in the watchlist
    old_symbol = old_symbol.upper()
    new_symbol = new_symbol.upper()
    if new_symbol not in available_stocks:
        print(f"{new_symbol} is not available")
        return
    if old_symbol in watchlist:
        # Remove the old symbol from the watchlist
        watchlist.remove(old_symbol)
        # Add the new symbol to the watchlist if it's not already there
        if new_symbol not in watchlist:
            watchlist.append(new_symbol)
            print(f"{old_symbol} has been updated to {new_symbol} in your watchlist.")
        else:
            print(f"{old_symbol} has been updated to {new_symbol}, which was already in your watchlist.")
    else:
        print(f"{old_symbol} is not in your watchlist.")

def delete_stock(symbol):  # remove a stock symbol from the watchlist

    symbol = symbol.upper()
    if symbol not in available_stocks:
        print(f"{symbol} is not available to operate on.")
        return
    if symbol in watchlist:
        watchlist.remove(symbol)
        print(f"{symbol} has been removed from your watchlist.")
    else:
        print(f"{symbol} is not in your watchlist.")

def display_watchlist(): # display watchlist and current price
  
    if watchlist:
        print("Your current watchlist:")
        for sym in watchlist:
            stock_data = get_stock_data(sym)
            if stock_data:
                price = stock_data['price']
                print(f"- {sym}: Current price is ${round(price, 2)}")
            else:
                print(f"- {sym}: Current price not available")
    else:
        print("Your watchlist is empty.")

def buy_stock(symbol, quantity): #buy stocks from the available stocks
    
    symbol = symbol.upper()
    if symbol not in available_stocks:
        print(f"{symbol} is not available to buy.")
        return False
    stock_data = get_stock_data(symbol)
    if stock_data:
        if symbol in portfolio:
            portfolio[symbol] += quantity
        else:
            portfolio[symbol] = quantity
        print(f"Bought {quantity} shares of {symbol} at ${round(stock_data['price'], 2)} per share.")
        return True
    else:
        print(f"Cannot buy {symbol}. Stock is not available.")
        return False

def sell_stock(symbol, quantity): # sell stocks from the portofolio
    
    symbol = symbol.upper()
    if symbol not in available_stocks:
        print(f"{symbol} is not available to sell.")
        return False
    if symbol in portfolio and portfolio[symbol] >= quantity:
        stock_data = get_stock_data(symbol)
        if stock_data:
            portfolio[symbol] -= quantity
            if portfolio[symbol] == 0:
                del portfolio[symbol]
            print(f"Sold {quantity} shares of {symbol} at ${round(stock_data['price'], 2)} per share.")
            return True
        else:
            print(f"Cannot sell {symbol}. Stock data not available.")
            return False
    else:
        print(f"You do not have enough shares of {symbol} to sell.")
        return False

def display_portfolio(): #display the value of the portofolio
 
    if portfolio:
        print("Your current portfolio:")
        total_value = 0
        for symbol, quantity in portfolio.items():
            stock_data = get_stock_data(symbol)
            if stock_data:
                market_value = stock_data['price'] * quantity
                total_value += market_value
                print(f"- {symbol}: {quantity} shares at ${round(stock_data['price'], 2)} per share, Total: ${round(market_value, 2)}")
            else:
                print(f"- {symbol}: {quantity} shares, Current price not available.")
        print(f"Total portfolio value: ${round(total_value, 2)}")
    else:
        print("Your portfolio is empty.")

def display_stock(): #display view menu
    while True:
        print("\nWhat you want to view?")
        print("1. View Market stocks")
        print("2. View Watchlist")
        print("3. View Your Portofolio")
        print("4. Exit View")

        display_choice = input("Enter your choice (1-3): ")

        if display_choice == "1":
            display_available_stocks()
            print()
        elif display_choice == "2":
            print()
            display_watchlist()
        elif display_choice == "3":
            print()
            display_portfolio()
        elif display_choice == "4":
            break

def display_available_stocks(): #display available stocks

    print("-------------Stocks Market------------")
    for symbol in available_stocks.keys():
        stock_data = get_stock_data(symbol)
        if stock_data:
            print(f"- {symbol}: ${round(stock_data['price'], 2)}")
        else:
            print(f"- {symbol}: Price not available")

# Initialize cash balance
user_cash = 10000.00  # Starting cash balance in USD

def menu():
    global user_cash

    initialize_prices()  # Initialize the stock prices at the start

    while True:
        print("\n--- Stock Portfolio Manager ---")
        print(f"Current Cash Balance: ${round(user_cash, 2)}")
        print("1. View stocks")
        print("2. Add stock to watchlist")
        print("3. Update stock in watchlist")
        print("4. Delete stock from watchlist")
        print("5. Buy stock")
        print("6. Sell stock")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1": #View Stocks
            display_stock()

        elif choice == "2": # add stock to watchlist

            print()
            display_available_stocks()
            print()
            display_watchlist()
            symbol = input("Enter the stock symbol to add to watchlist: ")
            add_stock(symbol)

        elif choice == "3": #update stocks to watchlist
            print()
            display_watchlist()
            old_symbol = input("Enter the stock symbol to update: ")
            new_symbol = input("Enter the new stock symbol: ")
            update_stock(old_symbol, new_symbol)

        elif choice == "4": #delete from watchlist
            print()
            display_watchlist()
            symbol = input("Enter the stock symbol to delete from watchlist: ")
            delete_stock(symbol)

        elif choice == "5": #buy stocks
            while True:
                display_available_stocks()
                symbol = input("Enter the stock symbol to buy: ").upper()
                if symbol not in available_stocks:
                    print(f"{symbol} is not available to buy.")
                    continue
                quantity = int(input(f"Enter the quantity of {symbol} to buy: "))
                stock_data = get_stock_data(symbol)
                if stock_data:
                    total_cost = stock_data['price'] * quantity
                    if user_cash >= total_cost:
                        success = buy_stock(symbol, quantity)
                        if success:
                            user_cash -= total_cost
                            print(f"Purchased {quantity} shares of {symbol} for ${round(total_cost, 2)}")
                            break
                    else:
                        print("Insufficient funds to complete the purchase.")

        elif choice == "6": #delete stocks
            while True:
                display_portfolio()
                symbol = input("Enter the stock symbol to sell: ").upper()
                if symbol not in available_stocks:
                    print(f"{symbol} is not available to sell.")
                    continue
                quantity = int(input(f"Enter the quantity of {symbol} to sell: "))
                if symbol in portfolio and portfolio[symbol] >= quantity:
                    stock_data = get_stock_data(symbol)
                    if stock_data:
                        total_revenue = stock_data['price'] * quantity
                        success = sell_stock(symbol, quantity)
                        if success:
                            user_cash += total_revenue
                            print(f"Sold {quantity} shares of {symbol} for ${round(total_revenue, 2)}")
                            break
                else:
                    print(f"Insufficient shares of {symbol} to sell.")
        elif choice == "7":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 to 7.")

# Run the menu function
if __name__ == "__main__":
    menu()
