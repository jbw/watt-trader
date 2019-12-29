# In Sword and Shield, Watt Traders can be found in the following Wild Area locations:
# Meetup Spot 47
# East Lake Axewell
# Dappled Grove
# Giant's Seat
# Bridge Field 25
# Hammerlocke Hills
# Giant's Cap
# Each Watt Trader's stock follows a schedule that changes daily,
# and always consists of one type of Poké Ball, a Wishing Piece, and five distinct TRs.
import math

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

from watt_trader.domain.traders import get_traders


def get_all_traders():
    return get_traders()


def get_all_traders_stock(first_tr_id, trader_id):
    all = {}

    first_tr_list = get_tr_list(first_tr_id)
    all[trader_id] = first_tr_list

    first_tr_id = first_tr_list[0]

    trader_ids = [0, 1, 2, 3, 4, 5, 6]

    if trader_id > TRADERS_MAX:
        raise Exception()
    if trader_id < TRADERS_MIN:
        raise Exception()

    for t_id in trader_ids:

        diff = abs(t_id - trader_id)

        if trader_id > t_id:
            tr_id = first_tr_id - (TRADERS_NEXT_TR_INCREMENT * diff)
            if tr_id < FIRST_TR_MIN:
                tr_id += FIRST_TR_TOTAL

        else:
            tr_id = (TRADERS_NEXT_TR_INCREMENT * diff) + first_tr_id
            if tr_id > FIRST_TR_MAX:
                tr_id -= FIRST_TR_TOTAL

        all[t_id] = get_tr_list(tr_id)

    return all


def get_tr_list(traders_first_tr_id):

    if traders_first_tr_id > TRADER_TR_MAX:
        raise Exception("TR ID max is: ", TRADER_TR_MAX)
    if traders_first_tr_id < TRADER_TR_MIN:
        raise Exception("TR ID min is: ", TRADER_TR_MIN)

    tr_increments = [0, 24, 42, 67, 96]

    return [
        traders_first_tr_id + tr_inc
        if traders_first_tr_id + tr_inc <= TRADER_TR_MAX
        else traders_first_tr_id + tr_inc - TRADER_TR_TOTAL
        for tr_inc in tr_increments
    ]


def get_all_traders_first_tr_ids(in_game_trader_first_tr_id):

    if in_game_trader_first_tr_id > FIRST_TR_MAX:
        raise Exception("TR ID max is: ", FIRST_TR_MAX)
    if in_game_trader_first_tr_id < FIRST_TR_MIN:
        raise Exception("TR ID min is: ", FIRST_TR_MIN)

    all = {}

    for trader_id in range(TRADERS_MIN, TRADERS_TOTAL, 1):
        all[trader_id] = _get_traders_first_tr_id(trader_id, in_game_trader_first_tr_id)

    return all


def _get_traders_first_tr_id(trader_id, in_game_trader_first_tr_id):

    tr_id_for_trader_id = in_game_trader_first_tr_id

    trader_id_start = 0
    while trader_id_start < trader_id:
        tr_id_for_trader_id = _get_next_first_tr_id(tr_id_for_trader_id)
        trader_id_start += 1

    return tr_id_for_trader_id


def _get_next_first_tr_id(first_tr_id):

    total = first_tr_id + TRADERS_NEXT_TR_INCREMENT

    if total >= FIRST_TR_MAX:
        total -= FIRST_TR_TOTAL

    return total
