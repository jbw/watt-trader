from pytest import fixture
from watt_trader.features.stock.list import get_all


@fixture()
def snapshot():

    # Snapshot in time
    in_game_trader_first_tr_id = 47
    snapshot = get_all(in_game_trader_first_tr_id)
    yield snapshot


def test_trader_0_returns_correct_tr_list(snapshot):
    # Meetup Spot
    assert snapshot[0] == [47, 71, 89, 14, 43]


def test_trader_1_returns_correct_tr_list(snapshot):
    # East Lake Axewell
    assert snapshot[1] == [4, 28, 46, 71, 0]


def test_trader_2_returns_correct_tr_list(snapshot):
    # Dappled Grove
    assert snapshot[2] == [11, 35, 53, 78, 7]


def test_trader_3_returns_correct_tr_list(snapshot):
    # Giant's Seat
    assert snapshot[3] == [18, 42, 60, 85, 14]


def test_trader_4_returns_correct_tr_list(snapshot):
    # Bridge Field 25
    assert snapshot[4] == [25, 49, 67, 92, 21]


def test_trader_5_returns_correct_tr_list(snapshot):
    # Hammerlocke Hills
    assert snapshot[5] == [32, 56, 74, 99, 28]


def test_trader_6_returns_correct_tr_list(snapshot):
    # Giant's Cap
    assert snapshot[6] == [39, 63, 81, 6, 35]
