import pytest
from watt_trader.domain.trader_trs import get_tr_list


def test_returns_tr_list_for_first_tr_id():

    # given
    first_tr_id = 47

    # when
    tr_list = get_tr_list(first_tr_id)

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
    tr_list = get_tr_list(first_tr_id)

    # then
    assert tr_list[3] == upper_tr_boundary
