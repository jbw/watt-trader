from pytest import fixture
from watt_trader.domain.trader_trs import get_tr_list, get_all_traders_stock


def assert_traders_tr_list(trader_tr_list):

    assert trader_tr_list[0] == [47, 71, 89, 14, 43]
    assert trader_tr_list[1] == [4, 28, 46, 71, 0]
    assert trader_tr_list[2] == [11, 35, 53, 78, 7]
    assert trader_tr_list[3] == [18, 42, 60, 85, 14]
    assert trader_tr_list[4] == [25, 49, 67, 92, 21]
    assert trader_tr_list[5] == [32, 56, 74, 99, 28]
    assert trader_tr_list[6] == [39, 63, 81, 6, 35]


def test_correct_stock_returns_for_trader_given_first_tr_id():

    # given
    first_tr = 4

    # when
    result = get_tr_list(first_tr)

    # then
    expect = [4, 28, 46, 71, 0]
    assert result == expect


def test_get_correct_stock_for_other_traders_given_first_tr_id_47_and_trader_id_0():

    # given
    first_tr = 47
    trader_id = 0

    # when
    result = get_all_traders_stock(first_tr, trader_id)

    # then
    assert_traders_tr_list(result)


def test_get_correct_stock_for_other_traders_given_first_tr_id_11_and_trader_id_1():

    # given
    first_tr = 4
    trader_id = 1

    # when
    result = get_all_traders_stock(first_tr, trader_id)

    # then
    assert_traders_tr_list(result)


def test_get_correct_stock_for_other_traders_given_first_tr_id_11_and_trader_id_2():

    # given
    first_tr = 11
    trader_id = 2

    # when
    result = get_all_traders_stock(first_tr, trader_id)

    # then
    assert_traders_tr_list(result)


def test_get_correct_stock_for_other_traders_given_first_tr_id_11_and_trader_id_3():

    # given
    first_tr = 18
    trader_id = 3

    # when
    result = get_all_traders_stock(first_tr, trader_id)

    # then
    assert_traders_tr_list(result)


def test_get_correct_stock_for_other_traders_given_first_tr_id_2_and_trader_id_4():

    # given
    first_tr = 25
    trader_id = 4

    # when
    result = get_all_traders_stock(first_tr, trader_id)

    # then
    assert_traders_tr_list(result)


def test_get_correct_stock_for_other_traders_given_first_tr_id_2_and_trader_id_5():

    # given
    first_tr = 32
    trader_id = 5

    # when
    result = get_all_traders_stock(first_tr, trader_id)

    # then
    assert_traders_tr_list(result)


def test_get_correct_stock_for_other_traders_given_first_tr_id_2_and_trader_id_6():

    # given
    first_tr = 39
    trader_id = 6

    # when
    result = get_all_traders_stock(first_tr, trader_id)

    # then
    assert_traders_tr_list(result)
