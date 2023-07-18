# MetaTrader5-Python

This is a README file for the project MetaTrader5-Python". The project provides functionality to interact with the MetaTrader 5 (MT5) platform using the MetaTrader5 library. It allows users to fetch current prices, retrieve historical data, access order book information, place buy and sell orders, and close positions. This README provides an overview of the project and explains how to use its different components.

## Installation

To use the MetaTrader5-Python" project, follow these installation steps:

1. Ensure that you have Python installed on your system (version X.X or higher).
2. Install the MetaTrader5 library by running the following command:
   ```
   pip install MetaTrader5
   ```
3. Download the project files from the GitHub repository:
   ```
   git clone https://github.com/username/project-name.git
   ```
   Replace "username" with your GitHub username and "project-name" with the actual name of the project.

## Usage

To use the MetaTrader5-Python" project, you need to import the necessary modules and classes and use them in your code. Below are code examples demonstrating the usage of each component:

### MetaTraderData

This class provides various methods to interact with the MT5 platform. To use it, import the `MetaTrader5` library and create an instance of the `MetaTraderData` class:

```python
import MetaTrader5 as mt5

class MetaTraderData:
    # Class methods and attributes...
```

### Initialization

To initialize the connection to the MT5 server, use the constructor of the `MetaTraderData` class:

```python
api = MetaTraderData(_login=10084329, _password='Dy41KitG', _server='B2Broker-MetaTrader5')
```

### Fetch Current Price

To fetch the current bid and ask prices of a symbol, use the `current_price` method:

```python
symbol = 'AAPL'
price = api.current_price(symbol)
print(price)  # Output: [bid_price, ask_price]
```

### Retrieve Historical Data

To retrieve historical data for a symbol within a specific timeframe, use the `historical_data` method:

```python
symbol = 'AAPL'
from_date = '2021-01-01'
to_date = '2021-12-31'
timeframe = 'H1'
data = api.historical_data(symbol, from_date, to_date, timeframe)
print(data)  # Output: DataFrame containing historical data
```

### Access Order Book Information

To retrieve the order book information for a symbol, use the `current_book` method:

```python
symbol = 'AAPL'
depth = 10
book = api.current_book(symbol, depth)
print(book)  # Output: DataFrame containing order book information
```

### Place Buy Order

To place a buy order for a symbol with a specific volume, use the `open_buy` method:

```python
symbol = 'AAPL'
volume = 100
result = api.open_buy(symbol, volume)
print(result)  # Output: [filled_volume, order_number]
```

### Place Sell Order

To place a sell order for a symbol with a specific volume, use the `open_sell` method:

```python
symbol = 'AAPL'
volume = 100
result = api.open_sell(symbol, volume)
print(result)  # Output: [filled_volume, order_number]
```

### Close Position

To close a position, use the `close_position` method:

```python
result = api.close_position()
print(result)  # Output: [filled_volume, order_number]
```

Please note that the above code examples assume that the MetaTrader5 library is properly installed and the connection to the MT5 server is established.

## Appendix

For additional information and resources, refer to the following:

- [MetaTrader5 Documentation](https://www.mql5.com/en/docs/integration/python_metatrader5)
- [MetaTrader5 Python
