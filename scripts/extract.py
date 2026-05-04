import yfinance as yf
import pandas as pd

def extract_stock_data(tickers=["PETR4.SA", "VALE3.SA", "ITUB4.SA"]):
    """Extrai dados históricos das ações selecionadas."""
    print(f"Iniciando extração para: {tickers}...")
    data = yf.download(tickers, period="1d", interval="1m")

    # Resetar o index para transformar o 'datetime' em coluna
    df = data.stack(level=1).reset_index()
    return df

if __name__ == "__main__":
    df_stocks = extract_stock_data()
    print(df_stocks.head())
