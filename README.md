AI & Tech Stock Screener
This project is a Python-based stock screener designed to identify promising AI and tech companies. It evaluates stocks against a set of fundamental and technical criteria, highlighting those with strong growth, profitability, and breakout potential. The screener processes a predefined list of AI & Tech stocks and provides categorized results for easy analysis.
Project Structure
ai-stock-screener/
│
├── main.py                     # Entry point to run the screener
├── requirements.txt            # Python dependencies
├── README.md                   # This documentation file
└── utils/
    ├── screener.py             # Core logic for data fetching, indicator calculation, and screening rules
    └── symbols.py              # List of AI & Tech stock tickers

Screening Criteria
The screener applies 5 key criteria to evaluate stocks:
Fundamental

EPS Growth (Year-over-Year): Must be greater than or equal to 15% (0.15).
Revenue Growth (Year-over-Year): Must be greater than or equal to 10% (0.10).
Net Profit Margin: Must be greater than or equal to 5% (0.05).
Free Cash Flow (FCF): Must be positive.

Technical

Price Breakout:
Current closing price is above its 50-day Simple Moving Average (SMA).
Current closing price exceeds the highest closing price in the last 20 trading days.



Setup Instructions
To get this project up and running on your local machine, follow these steps:

Clone the repository  
git clone https://github.com/your-username/ai-stock-screener.git
cd ai-stock-screener

(Note: Replace https://github.com/your-username/ai-stock-screener.git with your actual repository URL.)

Create a virtual environment (optional but recommended)Using a virtual environment helps manage project dependencies without conflicts with other Python projects.  
python3 -m venv venv

Activate the virtual environment:  

macOS/Linux: source venv/bin/activate  
Windows (Command Prompt): venv\Scripts\activate  
Windows (PowerShell): .\venv\Scripts\Activate.ps1


Install dependenciesOnce your virtual environment is active, install the required Python libraries:  
pip install -r requirements.txt

If you prefer to install manually:  
pip install yfinance pandas pandas-ta



Running the Screener
To execute the stock screener and view the results:  
python main.py

This script will:  

Load a predefined list of AI & Tech stock tickers from utils/symbols.py.  
Fetch historical price data and fundamental financial data for each stock from Yahoo Finance.  
Calculate technical indicators (like SMA) and fundamental growth rates.  
Evaluate each stock against the 5 screening criteria.  
Display categorized results in your console.

Sample Output
The output will be structured into three main sections:  
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

Next Steps & Ideas

Expand Stock Universe: Add more AI and Tech stock tickers to utils/symbols.py.
More Indicators: Integrate additional technical indicators (e.g., RSI, MACD, Bollinger Bands) or fundamental ratios (e.g., Debt-to-Equity, P/E Ratio) into screener.py.
Data Persistence: Save the screening results to a CSV, Excel file, or a local database.
Web Interface: Build a simple web application using frameworks like Streamlit or Flask to display the screener results in a user-friendly interface.
AI Integration: Explore using Large Language Models (LLMs) for advanced sentiment analysis of news, summarization of earnings calls, or even generating investment rationales for screened stocks.
Backtesting: Develop a module to backtest the screening strategy against historical data to evaluate its performance.

License
This project is open-source and provided as-is for educational and research purposes. Please conduct your own due diligence and verify any investment strategies independently.
Contact
Created by [Your Name]  
Founder of Skills Tech Talk  
Website: https://skillstechtalk.com  
Email: acodewell@skillstechtalk.com