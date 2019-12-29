from watt_trader.data import load_traders_csv, load_tr_csv

traders = load_traders_csv()
trs = load_tr_csv()


def get_traders():
    return traders


def get_traders_by_id(id):
    return [trader for trader in traders if trader["id"] == id][0]


def get_trs():
    return trs


def get_tr_by_id(id):
    return [tr for tr in trs if tr["id"] == id][0]
