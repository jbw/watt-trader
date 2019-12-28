from watt_trader.domain.trader_trs import get_tr_list, get_all_traders_first_tr_ids


def get_all(in_game_trader_first_tr_id):

    all_traders_first_tr_ids = get_all_traders_first_tr_ids(in_game_trader_first_tr_id)

    all = {}

    for trader_id in all_traders_first_tr_ids.keys():
        tr_id = all_traders_first_tr_ids[trader_id]
        all[trader_id] = get_tr_list(tr_id)

    return all
