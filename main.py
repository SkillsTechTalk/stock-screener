
from utils.screener import get_stock_data, get_fundamental_data, calculate_technical_indicators, screen_stock
from utils.symbols import symbols

def main():
    fundamentals_results = []
    technicals_results = []
    final_results = []

    for symbol in symbols:
        df = get_stock_data(symbol)
        fundamentals = get_fundamental_data(symbol)
        technicals = calculate_technical_indicators(df)

        if fundamentals and technicals:
            result = screen_stock(symbol, fundamentals, technicals)
            final_results.append(result)

            if result['details']['Technical Breakout']:
                technicals_results.append(result)
            if (
                fundamentals.get('eps_growth_yoy') and fundamentals['eps_growth_yoy'] >= 0.15 and
                fundamentals.get('revenue_growth_yoy') and fundamentals['revenue_growth_yoy'] >= 0.10 and
                fundamentals.get('net_profit_margin') and fundamentals['net_profit_margin'] >= 0.05 and
                fundamentals.get('fcf_positive')
            ):
                fundamentals_results.append(result)

    top_fundamentals = sorted(fundamentals_results, key=lambda x: x['details']['EPS Growth YoY'], reverse=True)[:10]
    top_technicals = technicals_results[:10]
    overlap = [x for x in top_fundamentals if x['ticker'] in [y['ticker'] for y in top_technicals]][:5]

    def print_results(title, data):
        print(f"\n=== {title} ===")
        for stock in data:
            print(f"{stock['ticker']} | EPS YoY: {stock['details']['EPS Growth YoY']}, Revenue YoY: {stock['details']['Revenue Growth YoY']}, Breakout: {stock['details']['Technical Breakout']}")

    print_results("Top 10 Fundamental Stocks", top_fundamentals)
    print_results("Top 10 Technical Breakout Stocks", top_technicals)
    print_results("Top 5 Overlap (Fundamental + Technical)", overlap)

if __name__ == "__main__":
    main()
