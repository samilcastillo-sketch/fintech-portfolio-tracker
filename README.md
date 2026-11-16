# Fintech Portfolio Analytics & Backtester

Quantitative portfolio tracking and risk modeling service. Computes net asset value, unrealized P&L, asset allocation weights, annualized volatility, and the Sharpe Ratio with zero external dependencies.

## Key Features

- **Interactive Financial Dashboard:** Visual asset breakdown with P&L badges and allocation weights.
- **Quantitative Risk Modeling:** Calculates Sharpe Ratio and annualized portfolio volatility.
- **RESTful Endpoints:** Retrieve full analytics snapshot or add new positions via `POST /api/v1/positions`.
- **Zero Third-Party Dependencies:** Pure standard library and lightweight HTML5 interface.

## Quickstart

```bash
# Start server
python3 -m src.server
```

Visit `http://localhost:5004` to see the live portfolio dashboard.

## Running Tests

```bash
python3 -m unittest discover tests -v
```
