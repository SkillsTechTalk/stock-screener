import yfinance as yf
import pandas as pd

# Define thresholds for screening criteria
SCREENING_THRESHOLDS = {
    'min_eps_growth_yoy': 0.10,
    'min_revenue_growth_yoy': 0.05,
    'min_net_profit_margin': 0.02,
    'min_fcf_positive': True,
    'technical_breakout_sma_length': 50,
    'technical_breakout_lookback_days': 20
}

def get_stock_data(ticker_symbol: str, period: str = "1y") -> pd.DataFrame:
    try:
        stock = yf.Ticker(ticker_symbol)
        df = stock.history(period=period)
        return df
    except Exception as e:
        print(f"  Error fetching historical data for {ticker_symbol}: {e}")
        return pd.DataFrame()

def get_fundamental_data(ticker_symbol: str) -> dict:
    try:
        stock = yf.Ticker(ticker_symbol)
        info = stock.info or {}

        net_income = info.get("netIncome", None)
        revenue = info.get("totalRevenue", None)
        eps_current = info.get("trailingEps", None)
        eps_forward = info.get("forwardEps", None)
        fcf = info.get("freeCashflow", 0)

        eps_growth_yoy = None
        if eps_current and eps_forward and eps_current != 0:
            eps_growth_yoy = (eps_forward - eps_current) / abs(eps_current)

        revenue_growth_yoy = info.get("revenueGrowth", None)
        net_profit_margin = (net_income / revenue) if revenue and net_income else None
        fcf_positive = fcf and fcf > 0

        return {
            'eps_growth_yoy': eps_growth_yoy,
            'revenue_growth_yoy': revenue_growth_yoy,
            'net_profit_margin': net_profit_margin,
            'fcf_positive': fcf_positive,
        }

    except Exception as e:
        print(f"  Error fetching fundamental data for {ticker_symbol}: {e}")
        return {}

def calculate_technical_indicators(df: pd.DataFrame) -> dict:
    if df.empty or 'Close' not in df.columns:
        return {}

    df['SMA_50'] = df['Close'].rolling(window=SCREENING_THRESHOLDS['technical_breakout_sma_length']).mean()
    lookback = SCREENING_THRESHOLDS['technical_breakout_lookback_days']
    recent_high = df['Close'].iloc[-lookback-1:-1].max() if len(df) > lookback else None
    latest_close = df['Close'].iloc[-1]
    latest_sma_50 = df['SMA_50'].iloc[-1]

    breakout = latest_close > latest_sma_50 and latest_close > recent_high if recent_high and latest_sma_50 else False

    return {
        'technical_breakout': breakout,
        'latest_close': latest_close,
        'latest_sma_50': latest_sma_50,
        'recent_high': recent_high
    }

def screen_stock(ticker_symbol: str, fundamentals: dict, technicals: dict) -> dict:
    passes = True
    reasons = []

    # EPS Growth
    eps = fundamentals.get('eps_growth_yoy')
    if eps is None or eps < SCREENING_THRESHOLDS['min_eps_growth_yoy']:
        passes = False
        reasons.append("EPS growth too low or missing")

    # Revenue Growth
    revenue = fundamentals.get('revenue_growth_yoy')
    if revenue is None or revenue < SCREENING_THRESHOLDS['min_revenue_growth_yoy']:
        passes = False
        reasons.append("Revenue growth too low or missing")

    # Profit Margin
    margin = fundamentals.get('net_profit_margin')
    if margin is None or margin < SCREENING_THRESHOLDS['min_net_profit_margin']:
        passes = False
        reasons.append("Profit margin too low or missing")

    # Free Cash Flow
    if not fundamentals.get('fcf_positive'):
        passes = False
        reasons.append("FCF not positive")

    # Technical Breakout
    if not technicals.get('technical_breakout'):
        passes = False
        reasons.append("No technical breakout")

    return {
        'ticker': ticker_symbol,
        'passes_screen': passes,
        'details': {
            'EPS Growth YoY': eps,
            'Revenue Growth YoY': revenue,
            'Net Profit Margin': margin,
            'FCF Positive': fundamentals.get('fcf_positive'),
            'Technical Breakout': technicals.get('technical_breakout')
        },
        'reasons_failed': reasons
    }
