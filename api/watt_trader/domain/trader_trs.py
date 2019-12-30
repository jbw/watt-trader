from watt_trader.domain.traders import get_traders, get_trs, get_traders_by_id, get_tr_by_id


TRADERS_MIN = 0
TRADERS_MAX = 6
TRADERS_TOTAL = 7

TRADERS_NEXT_TR_INCREMENT = 7

FIRST_TR_MAX = 49
FIRST_TR_MIN = 0
FIRST_TR_TOTAL = 50

TRADER_TR_MIN = 0
TRADER_TR_MAX = 99
TRADER_TR_TOTAL = 100


def get_tr_list(tr_ids_list):
    return [get_tr_by_id(tr_id) for tr_id in tr_ids_list]


def get_all_trs():
    return get_trs()


def get_all_traders():
    return get_traders()


def get_all_traders_stock(first_tr_id, selected_trader_id):

    _validate_first_tr_id(first_tr_id)
    _validate_trader_id(selected_trader_id)

    all_stock = {"stock": []}

    for trader_id in _get_trader_ids():

        steps = _get_steps_away_from_trader_id(trader_id, selected_trader_id)
        tr_id = _get_traders_first_tr_id_for_steps(first_tr_id, steps)

        trader_location = get_traders_by_id(trader_id)["name"]
        trs = get_tr_list(_get_tr_id_list(tr_id))

        all_stock["stock"].append({"trader_id": trader_id, "name": trader_location, "trs": trs})

    return all_stock


def _get_traders_first_tr_id_for_steps(tr_id, steps):

    if steps < 0:
        return _get_previous_traders_first_tr_id_for_steps(tr_id, abs(steps))

    return _get_next_traders_first_tr_id_for_steps(tr_id, steps)


def _get_steps_away_from_trader_id(trader_id, reference_point_trader_id):

    steps_from_reference_point = trader_id - reference_point_trader_id
    return steps_from_reference_point


def _get_next_traders_first_tr_id_for_steps(tr_id, steps):

    new_tr_id = tr_id
    for step in range(0, steps, 1):
        new_tr_id = _get_next_traders_first_tr_id(new_tr_id)

    return new_tr_id


def _get_next_traders_first_tr_id(tr_id):

    next_tr_id = tr_id + TRADERS_NEXT_TR_INCREMENT

    if next_tr_id > FIRST_TR_MAX:
        next_tr_id -= FIRST_TR_TOTAL
    return next_tr_id


def _get_previous_traders_first_tr_id_for_steps(tr_id, steps):

    new_tr_id = tr_id
    for step in range(0, steps, 1):
        new_tr_id = _get_previous_traders_first_tr_id(new_tr_id)

    return new_tr_id


def _get_previous_traders_first_tr_id(tr_id):

    next_tr_id = tr_id - TRADERS_NEXT_TR_INCREMENT

    if next_tr_id < FIRST_TR_MIN:
        next_tr_id += FIRST_TR_TOTAL

    return next_tr_id


def _get_tr_id_list(traders_first_tr_id):

    tr_increments = [0, 24, 42, 67, 96]

    return [
        traders_first_tr_id + tr_inc
        if traders_first_tr_id + tr_inc <= TRADER_TR_MAX
        else traders_first_tr_id + tr_inc - TRADER_TR_TOTAL
        for tr_inc in tr_increments
    ]


def _get_trader_ids():
    trader_ids = [trader["id"] for trader in get_traders()]
    return trader_ids


def _validate_first_tr_id(first_tr_id):

    if first_tr_id > FIRST_TR_MAX:
        raise Exception("TR ID max is: ", FIRST_TR_MAX)
    if first_tr_id < FIRST_TR_MIN:
        raise Exception("TR ID min is: ", FIRST_TR_MIN)


def _validate_trader_id(trader_id):
    if trader_id > TRADERS_MAX:
        raise Exception("Trader ID max is:", TRADERS_MAX)
    if trader_id < TRADERS_MIN:
        raise Exception("Trader ID min is:", TRADERS_MIN)
