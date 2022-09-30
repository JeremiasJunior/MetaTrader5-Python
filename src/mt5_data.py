import MetaTrader5 as mt5
import pandas as pd
from datetime import datetime 
import numpy as np


_login = 10041983
_password = 'Dy41KitG'
_server = 'B2Broker-MetaTrader5'

class MetaTraderData:

    def __init__(self, _login: int, _password = str, _server = str):
        self.login = _login
        self.password = _password
        self.server = _server

        try:
            mt5.initialize(login = self.login, password = self.password, server = self.server)
        except:
            print('error')
            quit()
    
    def __str__(self):
        return 'MetaTraderAPI'
    
    def current_price(self, symbol) -> tuple[float, float]:
        data = mt5.symbol_info_tick(symbol)
        data = data._asdict()
        data_bid = float(data['bid'])
        data_ask = float(data['ask'])

        return [data_bid, data_ask]
    

    @classmethod
    def TIMEFRAME(self, timeframe) -> int:

        if(timeframe == 'M1'): return mt5.TIMEFRAME_M1
        if(timeframe == 'M5'): return mt5.TIMEFRAME_M5
        if(timeframe == 'M10'): return mt5.TIMEFRAME_M10
        if(timeframe == 'M30'): return mt5.TIMEFRAME_M15
        if(timeframe == 'H1'): return mt5.TIMEFRAME_H1
        if(timeframe == 'M12'): return mt5.TIMEFRAME_H12
        if(timeframe == 'D1'): return mt5.TIMEFRAME_D1


    def historical_data(self, symbol:str, from_date:str, to_date:str, timeframe:str) -> pd.DataFrame():

        utc_from = datetime.fromisoformat(from_date)
        utc_to = datetime.fromisoformat(to_date)

        rates = mt5.copy_rates_range(symbol, self.TIMEFRAME(timeframe), utc_from, utc_to)
        
        df = pd.DataFrame(rates)
        df['date'] = df['time']
        df['date'] = df['date'].apply(lambda time: datetime.fromtimestamp(time))

        historical_data = df.set_index('date')
    
        return historical_data

    def current_book(self, symbol:str, len:int) -> pd.DataFrame():
        
        try:
            book = mt5.market_book_get(symbol)
        except:
            print("symbol doesn't exist!")

        book = mt5.market_book_get(symbol)
        book_ask = {'price':[], 'volume':[]}
        book_bid = {'price':[], 'volume':[]}

        for data in book:

            if(data[0] == 1):
                book_ask['price'].append(data[1])
                book_ask['volume'].append(data[2])
            if(data[0] == 2):
                book_bid['price'].append(data[1])
                book_bid['volume'].append(data[2])

        book_ask = pd.DataFrame(book_ask)[1:]
        book_bid = pd.DataFrame(book_bid)[1:]
        
        book_ask['deep'] = book_ask.index[::-1]
        book_ask.set_index('deep')
        
        book_bid['deep'] = -(book_bid.index[::-1])
        book_bid.set_index('deep')

        result = pd.concat([book_bid, book_ask], axis=0)
        result = result.set_index('deep')
        result = result.sort_index(ascending=False)

        



