# AI & Tech Stock Screener


This project is a Python-based stock screener designed
to identify promising AI and tech companies. 
It evaluates stocks against a set of fundamental
and technical criteria, highlighting those with 
strong growth, profitability, and breakout potential. 
The screener processes a predefined list of AI & Tech 
stocks and provides categorized results for easy
analysis.

---

## Screening Criteria

The screener applies **5 key criteria** to evaluate stocks:

### Fundamental

- **EPS Growth (Year-over-Year)**: Must be ≥ 15% (`0.15`)
- **Revenue Growth (Year-over-Year)**: Must be ≥ 10% (`0.10`)
- **Net Profit Margin**: Must be ≥ 5% (`0.05`)
- **Free Cash Flow (FCF)**: Must be **positive**

### Technical

- **Price Breakout**:
  - Closing price is **above its 50-day Simple Moving Average (SMA)**
  - Closing price **exceeds the highest closing price** in the last 20 trading days

---

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install yfinance pandas pandas-ta
```

---

## Running the Screener

To execute the stock screener and view the results:

```bash
python main.py
```

This script will:

* Load a predefined list of AI & Tech stock tickers from `utils/symbols.py`
* Fetch historical price and financial data from Yahoo Finance
* Calculate technical indicators (like SMA) and growth metrics
* Evaluate stocks against the 5 screening criteria
* Display categorized results in your console

---

## Sample Output

```text
=== Top 10 Fundamental Stocks ===
AAPL | EPS YoY: 0.25, Revenue YoY: 0.12, Breakout: True
MSFT | EPS YoY: 0.18, Revenue YoY: 0.11, Breakout: True
...

=== Top 10 Technical Breakout Stocks ===
NVDA | EPS YoY: 0.78, Revenue YoY: 0.93, Breakout: True
SNOW | EPS YoY: 0.30, Revenue YoY: 0.29, Breakout: True
...

=== Top 5 Overlap (Fundamental + Technical) ===
MSFT | EPS YoY: 0.18, Revenue YoY: 0.11, Breakout: True
AMD | EPS YoY: 0.22, Revenue YoY: 0.15, Breakout: True
...
```

---

## Next Steps & Ideas

* **Expand Stock Universe**: Add more AI and Tech tickers to `utils/symbols.py`
* **More Indicators**: Integrate RSI, MACD, Bollinger Bands, Debt-to-Equity, etc.
* **Data Persistence**: Save results to CSV, Excel, or a local DB
* **Web Interface**: Build a UI with Streamlit or Flask
* **AI Integration**: Use LLMs for summarizing earnings/news or generating stock rationale
* **Backtesting**: Add historical performance analysis of screened strategies

---

## License

This project is open-source and provided **as-is** for educational and research purposes. Please perform your own due diligence before making investment decisions.

---

## Contact

Website: [https://skillstechtalk.com](https://skillstechtalk.com)

Email: [acodewell@skillstechtalk.com](mailto:acodewell@skillstechtalk.com)

```
```
