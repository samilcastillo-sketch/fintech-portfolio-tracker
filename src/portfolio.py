"""
Financial Portfolio Analytics & Backtesting Engine
"""
import math
from typing import List, Dict, Any

class PortfolioEngine:
    def __init__(self):
        # Sample market prices
        self.market_prices = {
            "BTC": 91500.0,
            "ETH": 3150.0,
            "NVDA": 145.0,
            "AAPL": 225.0,
            "TSLA": 340.0,
            "USDC": 1.0
        }
        self.positions: List[Dict[str, Any]] = [
            {"symbol": "BTC", "quantity": 0.45, "buy_price": 64000.0},
            {"symbol": "ETH", "quantity": 3.5, "buy_price": 2800.0},
            {"symbol": "NVDA", "quantity": 50.0, "buy_price": 110.0},
            {"symbol": "AAPL", "quantity": 30.0, "buy_price": 190.0},
            {"symbol": "USDC", "quantity": 8000.0, "buy_price": 1.0}
        ]

    def calculate_summary(self) -> Dict[str, Any]:
        total_invested = 0.0
        current_value = 0.0
        breakdown = []

        for p in self.positions:
            sym = p["symbol"]
            qty = p["quantity"]
            buy_price = p["buy_price"]
            curr_price = self.market_prices.get(sym, buy_price)

            invested = qty * buy_price
            val = qty * curr_price
            pnl = val - invested
            pnl_pct = (pnl / invested) * 100 if invested > 0 else 0.0

            total_invested += invested
            current_value += val

            breakdown.append({
                "symbol": sym,
                "quantity": qty,
                "buy_price": buy_price,
                "current_price": curr_price,
                "invested": round(invested, 2),
                "current_value": round(val, 2),
                "pnl": round(pnl, 2),
                "pnl_pct": round(pnl_pct, 2)
            })

        # Calculate asset allocation weights
        for b in breakdown:
            b["weight_pct"] = round((b["current_value"] / current_value) * 100, 1) if current_value > 0 else 0

        total_pnl = current_value - total_invested
        total_pnl_pct = (total_pnl / total_invested) * 100 if total_invested > 0 else 0.0

        # Risk metrics simulation
        annualized_return = 0.285  # 28.5%
        risk_free_rate = 0.045     # 4.5% US Treasury
        volatility = 0.165         # 16.5% standard deviation
        sharpe_ratio = round((annualized_return - risk_free_rate) / volatility, 2)

        return {
            "total_invested": round(total_invested, 2),
            "current_value": round(current_value, 2),
            "total_pnl": round(total_pnl, 2),
            "total_pnl_pct": round(total_pnl_pct, 2),
            "sharpe_ratio": sharpe_ratio,
            "annualized_volatility_pct": round(volatility * 100, 1),
            "positions": breakdown
        }

    def add_position(self, symbol: str, quantity: float, buy_price: float):
        if quantity <= 0 or buy_price <= 0:
            raise ValueError("Quantity and buy price must be positive.")
        self.positions.append({
            "symbol": symbol.upper(),
            "quantity": float(quantity),
            "buy_price": float(buy_price)
        })
        return self.calculate_summary()
