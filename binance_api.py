import requests as r
import config as defs
import db


class BinanceAPI:
    def __init__(self):
        self.url = defs.BINANCE_URL
        self.db = db.DB()

    def obDepth(self, symbol):
        ep = f'{self.url}api/v3/depth?symbol={symbol}'
        rsp = r.get(ep)
        j = rsp.json()
        for _ in j['bids']:
            pr = _[0]
            qnt =  _[1]
            self.db.addPrice(price=pr, qnt=qnt, b_o_a='BID')
        for _ in j['asks']:
            pr = _[0]
            qnt = _[1]
            self.db.addPrice(price=pr, qnt=qnt, b_o_a='ASK')

    def price(self, symbol):
        ep = f'{self.url}api/v3/ticker/price?symbol={symbol}'
        rsp = r.get(ep)
        # print(rsp.json())
        # print(rsp.status_code)
        return round(float(rsp.json()['price']), 2)