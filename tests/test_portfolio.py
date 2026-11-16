"""
Automated Test Suite for Fintech Portfolio Tracker
"""
import unittest
from src.portfolio import PortfolioEngine

class TestPortfolioEngine(unittest.TestCase):
    def test_calculate_summary_returns_metrics(self):
        engine = PortfolioEngine()
        summary = engine.calculate_summary()

        self.assertGreater(summary["total_invested"], 0)
        self.assertGreater(summary["current_value"], 0)
        self.assertIn("positions", summary)
        self.assertIn("sharpe_ratio", summary)

        # Check weight sum is ~100%
        total_weight = sum(p["weight_pct"] for p in summary["positions"])
        self.assertAlmostEqual(total_weight, 100.0, delta=1.5)

    def test_add_position_updates_metrics(self):
        engine = PortfolioEngine()
        initial_count = len(engine.positions)
        engine.add_position("SOL", 10.0, 180.0)
        self.assertEqual(len(engine.positions), initial_count + 1)

if __name__ == "__main__":
    unittest.main()
