import pandas as pd

def transform_data(df):
    """realiza a limpeza e cria indicadores financeiros"""

    # 1. garante que não teremos valores nulos
    df = df.dropna()

    # 2. calcula a variação Percentual (volatility)
    # usamos o preço de fechamento 'close'
    df['Daily_Return'] = df['Close'].pct_change()

    # 3. Média Móvel Simples (SMA) de 5 períodos 
    df ['SMA_5'] = df['Close'].rolling(window=5).mean()

    print("Transformação concluída com sucesso.")
    return df