import MetaTrader5 as mt5
import pandas as pd


_login = 10041983
_password = 'Dy41KitG'
_broker = 'B2Broker-MetaTrader5'

class MetaTraderData:
    def __init__(self, _login: int, _password = str, _server = str):
        self.login = _login
        self.password = _password
        self.server = _broker
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
    def tf_converter(self, timeframe:str):
        pass
    def historical_data(self, symbol, date_from, date_to, timeframe):
        
        rates = mt5.market_book_get(symbol)

        pass

        
        


metatrader = MetaTraderData(_login, _password, _server)


for i in range(10):
    print(metatrader.current_price('BTCUSD'))