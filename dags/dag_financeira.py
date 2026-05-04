import os
import sys
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

# --- SOLUÇÃO DE CAMINHO ---
# Pega o caminho da pasta atual (dags) e sobe um nível para a raiz (FINANCAS_ECO)
root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if root_path not in sys.path:
    sys.path.insert(0, root_path)

# Agora o import deve funcionar
try:
    from scripts.extract import extract_stock_data
    from scripts.transform import transform_data
    from scripts.load import load_data
except ImportError as e:
    print(f"Erro ao importar scripts: {e}")
# --------------------------

def pipeline_completo():
    df_raw = extract_stock_data()
    df_transformed = transform_data(df_raw)
    load_data(df_transformed)

with DAG(
    dag_id='meu_primeiro_pipeline_financeiro',
    start_date=datetime(2023, 1, 1),
    schedule_interval='@daily',
    catchup=False
) as dag:

    tarefa_etl = PythonOperator(
        task_id='executar_etl_completo',
        python_callable=pipeline_completo
    )
