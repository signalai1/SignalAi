from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# Starter market catalog. Live Kalshi quotes and TradingView data are not connected yet.
MARKETS = {
    "commodities": [
        {"symbol": "GOLD", "name": "Gold", "category": "Commodities"},
        {"symbol": "SILVER", "name": "Silver", "category": "Commodities"},
        {"symbol": "COPPER", "name": "Copper", "category": "Commodities"},
        {"symbol": "PALLADIUM", "name": "Palladium", "category": "Commodities"},
        {"symbol": "OIL", "name": "Crude Oil", "category": "Commodities"},
        {"symbol": "NATGAS", "name": "Natural Gas", "category": "Commodities"},
    ],
    "crypto": [
        {"symbol": "BTC", "name": "Bitcoin", "category": "Crypto"},
        {"symbol": "ETH", "name": "Ethereum", "category": "Crypto"},
        {"symbol": "SOL", "name": "Solana", "category": "Crypto"},
        {"symbol": "XRP", "name": "XRP", "category": "Crypto"},
        {"symbol": "DOGE", "name": "Dogecoin", "category": "Crypto"},
    ],
}

@app.get("/")
def home():
    return render_template("index.html")

@app.get("/api/markets")
def markets():
    category = request.args.get("category", "commodities").lower()
    if category not in MARKETS:
        return jsonify({"error": "Unknown category"}), 400
    return jsonify(MARKETS[category])

@app.get("/health")
def health():
    return jsonify({"status": "ok", "service": "Signal AI"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port= int(__import__("os").environ.get("PORT", 5000)))
