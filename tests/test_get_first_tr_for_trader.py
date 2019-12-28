import pytest
from watt_trader.domain.trader_trs import _get_traders_first_tr_id, get_all_traders_first_tr_ids


def test_it_should_wrap_around_the_tr_boundary_of_0_and_49():

    # given
    tr_id = 47

    # when
    next_tr_id = get_all_traders_first_tr_ids(tr_id)[1]

    # then
    assert next_tr_id == 4


def test_it_should_return_tr_id_on_lower_boundary_of_0_and_49():

    # given
    tr_id = 0

    # when
    next_tr_id = get_all_traders_first_tr_ids(tr_id)[1]

    # then
    assert next_tr_id == 7


def test_it_should_return_tr_id_on_upper_boundary_of_0_and_49():

    # given
    tr_id = 49

    # when
    next_tr_id = get_all_traders_first_tr_ids(tr_id)[1]

    # then
    assert next_tr_id == 6


def test_it_should_throw_if_tr_id_is_greater_than_tr_boundary_of_0_and_49():
    with pytest.raises(Exception):

        # given
        tr_id = -1

        # when/then
        get_all_traders_first_tr_ids(tr_id)


def test_it_should_throw_if_tr_id_is_less_than_tr_boundary_of_0_and_49():
    with pytest.raises(Exception):

        # given
        tr_id = 50

        # when/then
        get_all_traders_first_tr_ids(tr_id)
