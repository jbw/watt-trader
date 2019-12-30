from watt_trader.domain.trader_trs import get_all_traders_stock
from watt_trader.domain.trader_trs import get_all_trs


def get_all_stock_by_trader(first_tr_id, trader_id):

    all_trs = get_all_trs()

    stock = get_all_traders_stock(first_tr_id, trader_id)

    trs_in_circulation = [stock["trs"] for stock in stock["stock"]]
    trs_in_circulation = [j for sub in trs_in_circulation for j in sub]

    not_in_circulation = list(filter(lambda it: it not in trs_in_circulation, all_trs))

    stock["not_in_circulation"] = not_in_circulation

    return stock
