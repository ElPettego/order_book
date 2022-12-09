from pymongo import MongoClient
import config as defs

class DB: 
    def __init__(self):
        self.client = MongoClient()
        self.order_book_db = self.client.order_book_db
        self.order_book = self.order_book_db.order_book
    
    def flush(self):
        self.order_book.delete_many({})

    def addPrice(self, price, qnt, b_o_a):
        doc = {
            "price": round(float(price), 2),
            "quantity": round(float(qnt), 2),
            "bid/ask": b_o_a
        }
        self.order_book.insert_one(doc)

    def findBidAsk(self, b_o_a):
        q = []
        for ind, d in enumerate(self.order_book.find({"bid/ask": b_o_a})):
            if ind == defs.OB_BOUNDS:
                return q
            q.append(d)

