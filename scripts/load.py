import pandas as pd
from sqlalchemy import create_engine

def load_data(df, db_name="finance_database.db"):
    """Salva os dados transformados em um banco de dados SQL local."""
    print(f"Iniciando carga no banco {db_name}...")
    
    # Criamos a conexão com o SQLite
    # O arquivo será criado na raiz do seu projeto
    engine = create_engine(f'sqlite:///{db_name}')
    
    # Salva o DataFrame na tabela 'stock_history'
    # if_exists='append' adiciona dados novos sem apagar os antigos
    df.to_sql('stock_history', con=engine, if_exists='append', index=False)
    
    print(f"Sucesso! {len(df)} linhas inseridas no banco.")
