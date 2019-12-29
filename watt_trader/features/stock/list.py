from watt_trader.domain.trader_trs import get_all_traders_stock


def get_all_stock_by_trader(first_tr_id, trader_id):
    return get_all_traders_stock(first_tr_id, trader_id)
