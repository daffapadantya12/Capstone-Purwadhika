
# Stock Management Program

## Overview

This program simulates a stock portfolio management system, allowing users to monitor a stock watchlist, manage a portfolio, and interact with stock prices. It provides functionalities for viewing, buying, and selling stocks while simulating stock price updates.

## Features

- **Watchlist Management**: Monitor stock symbols of interest.
- **Portfolio Management**: Track owned stocks and their quantities.
- **Simulated Stock Prices**: Work with randomly generated stock prices for available stocks.
- **Buy/Sell Operations**: Execute buy and sell orders based on available stocks.

## Requirements

- Python 3.6 or higher

## Installation

1. Clone or download this repository.
2. Ensure you have Python installed on your machine.
3. Run the script using the following command:
   ```bash
   python StockApp.py
   ```

## Usage

1. **Watchlist**:
   - Contains predefined stocks such as `AAPL`, `MSFT`, and more.
   - Add or remove stocks from your watchlist as needed.

2. **Portfolio**:
   - Tracks the stocks you own and their quantities.
   - Preloaded with some example stocks like `AAPL`, `GOOGL`, and others.

3. **Available Stocks**:
   - Displays a list of stocks available for trading with their simulated prices.

4. **Buying and Selling**:
   - Buy stocks using their ticker symbols and update your portfolio.
   - Sell stocks you own to adjust your portfolio holdings.

5. **Simulated Prices**:
   - Stock prices are dynamically generated, simulating real market behavior.

## Example

- View the watchlist:
  ```plaintext
  Watchlist: ['AAPL', 'MSFT', 'AMZN', 'NVDA', 'TSLA']
  ```

- Check portfolio:
  ```plaintext
  Portfolio: {'AAPL': 5, 'GOOGL': 7, 'MSFT': 2, 'AMZN': 3}
  ```

- Check available stock prices:
  ```plaintext
  Available Stocks: {'AAPL': 150.00, 'GOOGL': 179.00, 'MSFT': 300.00, 'AMZN': 350.00, 'META': 350.00, 'TSLA': 700.00}
  ```

- Execute a buy or sell transaction through menu options or direct commands.

## Customization

You can customize the following:
- Add or remove stocks in the `watchlist`.
- Modify initial portfolio stocks and quantities.
- Adjust stock prices or introduce new stock symbols in `available_stocks`.

## Contributing

Feel free to contribute by:
- Adding new features like real-time stock price fetching using APIs.
- Improving the UI for better interactivity.
- Enhancing simulation logic for stock price variations.

## License

This project is licensed under the MIT License.
