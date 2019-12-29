from watt_trader.domain.trader_trs import (
    _get_next_traders_first_tr_id,
    _get_previous_traders_first_tr_id,
    _get_previous_traders_first_tr_id_for_steps,
    _get_next_traders_first_tr_id_for_steps,
    _get_steps_away_from_trader_id,
)


def test_it_should_wrap_around_the_tr_boundary_of_0_and_49():

    # given
    tr_id = 47

    # when
    next_tr_id = _get_next_traders_first_tr_id(tr_id)

    # then
    assert next_tr_id == 4


def test_it_should_return_tr_id_on_lower_boundary_of_0_and_49():

    # given
    tr_id = 0

    # when
    next_tr_id = _get_next_traders_first_tr_id(tr_id)

    # then
    assert next_tr_id == 7


def test_it_should_return_tr_id_on_upper_boundary_of_0_and_49():

    # given
    tr_id = 49

    # when
    next_tr_id = _get_next_traders_first_tr_id(tr_id)

    # then
    assert next_tr_id == 6


def test_it_should_return_previous_traders_tr_id():

    # given
    tr_id = 4

    # when
    next_tr_id = _get_previous_traders_first_tr_id(tr_id)

    # then
    assert next_tr_id == 47


def test_it_should_return_previous_traders_tr_id_by_1_step_back():

    # given
    tr_id = 4

    # when
    next_tr_id = _get_previous_traders_first_tr_id_for_steps(tr_id, 1)

    # then
    assert next_tr_id == 47


def test_it_should_return_previous_traders_tr_id_by_2_step_back():

    # given
    tr_id = 11

    # when
    next_tr_id = _get_previous_traders_first_tr_id_for_steps(tr_id, 2)

    # then
    assert next_tr_id == 47


def test_it_should_return_previous_traders_tr_id_by_6_step_back():

    # given
    tr_id = 39

    # when
    next_tr_id = _get_previous_traders_first_tr_id_for_steps(tr_id, 6)

    # then
    assert next_tr_id == 47


def test_it_should_return_next_traders_tr_id_by_6_step_back():

    # given
    tr_id = 47

    # when
    next_tr_id = _get_next_traders_first_tr_id_for_steps(tr_id, 6)

    # then
    assert next_tr_id == 39


def test_trader_6_is_6_steps_away_from_trader_0():

    # given/when
    steps = _get_steps_away_from_trader_id(0, 6)

    # then
    assert steps == -6


def test_trader_1_is_1_steps_away_from_trader_0():

    # given/when
    steps = _get_steps_away_from_trader_id(0, 1)

    # then
    assert steps == -1


def test_trader_0_is_3_steps_away_from_trader_3():

    # given/when
    steps = _get_steps_away_from_trader_id(3, 0)

    # then
    assert steps == 3
