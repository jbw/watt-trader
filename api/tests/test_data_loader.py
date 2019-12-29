from watt_trader.data import load_tr_csv, load_traders_csv


def test_loads_traders_data():

    # given/when
    trader_list = load_traders_csv()

    # then
    assert trader_list[0]["id"] == 0
    assert trader_list[0]["location"] == "Meetup Spot"


def test_loads_tr_data():

    # given/when
    tr_list = load_tr_csv()

    # then
    assert tr_list[0]["id"] == 0
    assert tr_list[0]["code"] == "TR00"
    assert tr_list[0]["name"] == "Swords Dance"
    assert tr_list[0]["cost"] == "2000"
