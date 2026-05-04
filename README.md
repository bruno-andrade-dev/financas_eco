# 🚀 Finance Data Pipeline: ETL & Orquestração com Airflow

Este projeto demonstra a construção de um ecossistema de dados robusto para o setor financeiro. O objetivo é automatizar a coleta, processamento e armazenamento de indicadores de mercado, utilizando as melhores práticas de engenharia de dados.

## 🛠️ Tecnologias Utilizadas

*   **Python 3.10**: Linguagem base para o desenvolvimento de toda a lógica de dados.
*   **Pandas**: Utilizado para manipulação de DataFrames, limpeza e criação de indicadores técnicos.
*   **YFinance**: Biblioteca para consumo de dados em tempo real da B3 e mercados globais.
*   **SQLAlchemy**: Engine de comunicação com o banco de dados para garantir persistência eficiente.
*   **Apache Airflow**: Orquestrador líder de mercado utilizado para gerir as dependências e o agendamento das tarefas.
*   **Docker & Docker Compose**: Garantia de que o ambiente é isolado e reprodutível em qualquer máquina.

## 🏗️ Arquitetura do Pipeline

O pipeline segue o padrão clássico **ETL (Extract, Transform, Load)**:

1.  **Extração**: O script consome a API do Yahoo Finance para capturar cotações de ativos como PETR4, VALE3 e ITUB4 com granularidade de 1 minuto.
2.  **Transformação**: Os dados brutos passam por um processo de limpeza e enriquecimento, onde calculamos a **Variação Percentual Diária** e a **Média Móvel Simples (SMA)**.
3.  **Carga**: Os dados processados são inseridos num banco de dados relacional (SQLite/PostgreSQL), utilizando a estratégia de *append* para manter o histórico.
4.  **Orquestração**: Através do Airflow, definimos uma **DAG** que monitoriza a execução e permite retentativas em caso de falha.

## 📂 Estrutura do Projeto

```text
FINANCAS_ECO/
├── dags/               # Definição do fluxo e agendamento no Airflow
│   └── dag_financeira.py
├── scripts/            # Lógica modular do processo (Python puro)
│   ├── __init__.py
│   ├── extract.py      # Módulo de extração de dados
│   ├── transform.py    # Módulo de lógica de negócio
│   └── load.py         # Módulo de persistência SQL
├── docker-compose.yaml # Configuração da infraestrutura de containers
├── Dockerfile          # Imagem customizada com dependências instaladas
├── main.py             # Ponto de entrada para testes locais rápidos
└── requirements.txt    # Lista de dependências do projeto
```

## 🚀 Como Executar

### Pré-requisitos
*   Docker Desktop instalado e em execução.

### Instalação
1. Clone este repositório:
   ```bash
   git clone https://github.com
   ```
2. Inicie o ambiente (isso fará o build da imagem e subirá o Airflow):
   ```bash
   docker-compose up -d --build
   ```
3. Aceda ao painel do Airflow em: `http://localhost:8080`
4. Use as credenciais geradas (padrão `admin` / `admin` ou consulte os logs do container).

---
**Desenvolvido por Bruno Andrade**
