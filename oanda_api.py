import requests
import config as defs

class OandaAPI:
    def __init__(self):
        self.token = defs.OANDA_API
        self.url = defs.OANDA_URL
        self.session = requests.Session()
        self.session.headers.update({
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json'
        }) 

    def orderBook(self, pair):
        ep = f'{self.url}v3/instruments/{pair}/orderBook'
        r = self.session.get(url=ep)
        return r.json()