from scripts.extract import extract_stock_data
from scripts.transform import transform_data
from scripts.load import load_data

def run_pipeline():
    print("--- [PASSO 1] Extração ---")
    data_raw = extract_stock_data()
    
    if data_raw.empty:
        print("Erro: Nenhum dado extraído.")
        return

    print("\n--- [PASSO 2] Transformação ---")
    data_processed = transform_data(data_raw)
    
    print("\n--- [PASSO 3] Carga ---")
    load_data(data_processed)
    
    print("\n✅ Pipeline concluído com sucesso!")

if __name__ == "__main__":
    run_pipeline()
