from watt_trader.domain.trader_trs import _get_tr_id_list, get_all_traders


def test_returns_tr_list_for_first_tr_id():

    # given
    first_tr_id = 47

    # when
    tr_list = _get_tr_id_list(first_tr_id)

    # then
    assert tr_list[0] == 47
    assert tr_list[1] == 71
    assert tr_list[2] == 89
    assert tr_list[3] == 14
    assert tr_list[4] == 43


def test_returns_tr_list_for_upper_boundary():

    # given
    upper_tr_boundary = 99
    first_tr_id = 32

    # when
    tr_list = _get_tr_id_list(first_tr_id)

    # then
    assert tr_list[3] == upper_tr_boundary


def test_returns_all_traders():

    # given
    all_traders = get_all_traders()

    # when
    trader_location = all_traders[0]["location"]

    # then
    assert trader_location == "Meetup Spot"
