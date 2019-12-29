import csv


def _load_csv(path):
    rows = []
    with open(path, "r") as trs_csv:
        reader = csv.DictReader(trs_csv)
        for row in reader:
            row["id"] = int(row["id"])
            rows.append(row)
    return rows


def load_tr_csv():
    return _load_csv("./watt_trader/data/trs.csv")


def load_traders_csv():
    return _load_csv("./watt_trader/data/traders.csv")
