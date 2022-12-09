import oanda_api as oa
import binance_api as ba
import config as defs
import os
from colorama import Back
import time
import db


def main():
    # oa_o = oa.OandaAPI()
    bi_o = ba.BinanceAPI()
    db_o = db.DB()
    bg_ask = None
    bg_bid = None
    trend = None
    while True:
        all_ask_q = 0
        all_bid_q = 0
        db_o.flush()
        bi_o.obDepth(defs.ASSET)
        cp = bi_o.price(defs.ASSET)
        os.system('cls')
        print(f'{Back.CYAN}CURRENT PRICE {defs.ASSET}: {cp}{Back.RESET}'.center(
            defs.TERMINAL_WIDTH))
        print(f'{Back.MAGENTA}{"BID QNT" : <20} {"BID PRICE" : <30} {"ASK PRICE" : >30} {"ASK QNT" : >20}{Back.RESET}')
        bid = db_o.findBidAsk('BID')
        ask = db_o.findBidAsk('ASK')
        # print(bid)
        # print(ask)
        for i in range(0, defs.OB_BOUNDS):            
            bid_q = bid[i]['quantity']
            bid_p = bid[i]['price']
            ask_q = ask[i]['quantity']
            ask_p = ask[i]['price']
            all_ask_q += ask_q
            all_bid_q += bid_q
            if all_bid_q > all_ask_q:
                bg_ask = Back.GREEN
                bg_bid = Back.RED
                trend = Back.RED
            else:
                bg_ask = Back.RED
                bg_bid = Back.GREEN
                trend = Back.GREEN
            if ask_q > 1 or bid_q > 1:
                print(f'{Back.GREEN}{bid_q : <20} | {bid_p : <30}{Back.RESET}',
                    f'{Back.RED}{ask_p : >30} | {ask_q : >20}{Back.RESET}',
                    f'TOT BID: {bg_bid}{round(all_bid_q, 2) : >8}{Back.RESET} - TOT ASK: {bg_ask}{round(all_ask_q, 2) : >8}{Back.RESET} | T = {trend}-{Back.RESET}')
        time.sleep(5)


if __name__ == '__main__':
    main()
