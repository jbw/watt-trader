from flask import Flask, jsonify
from watt_trader.features.stock.list import get_all_stock_by_trader
from watt_trader.features.traders.list import get_all as get_all_traders
from watt_trader.features.trs.list import get_all as get_all_trs

app = Flask(__name__)


@app.route("/api/trs", methods=["GET"])
def get_trs():
    return jsonify(get_all_trs())


@app.route("/api/traders", methods=["GET"])
def get_traders():
    return jsonify(get_all_traders())


@app.route("/api/stock/<int:trader_id>/<int:tr_id>", methods=["GET"])
def get_by_trader_and_tr_id(trader_id, tr_id):
    return jsonify(get_all_stock_by_trader(tr_id, trader_id))


if __name__ == "__main__":
    app.run(debug=True)
