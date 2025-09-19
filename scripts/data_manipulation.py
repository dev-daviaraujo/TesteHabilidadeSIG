# Importando a lib do Pandas 
import pandas as pd 
 
import sys 
from pathlib import Path 

# Adiciona a raiz do projeto ao sys.path 
sys.path.append(str(Path(__file__).resolve().parent.parent)) 

# Importando a Query SQL e arquivo de conexão ao SQL Server 
from scripts.db_connection import get_connection 
from queries.consultaSIG import QUERY_VENDAS 

def carregar_dados(): 
    conn = get_connection() 
    df = pd.read_sql(QUERY_VENDAS, conn)     
    df["OrderDate"] = pd.to_datetime(df["OrderDate"])      
    return df 

def resumo_vendas(df): 
    # vendas por região/produto 
    vendas_regiao_produto = ( 
        df.groupby(["Region", "ProductName"])["TotalDue"].sum().reset_index() ) 
    
    # vendas por ano/mês 
    df["ano"] = df["OrderDate"].dt.year 
    df["mes"] = df["OrderDate"].dt.month 
    vendas_periodo = ( df.groupby(["ano", "mes"])["TotalDue"].sum().reset_index() ) 
    
    print(vendas_periodo.head()) 
    print(vendas_regiao_produto.head()) 
    return vendas_regiao_produto, vendas_periodo

if __name__ == "__main__":
    # Carrega os dados
    df_vendas = carregar_dados()
    
    # Gera os resumos
    vendas_regiao_produto, vendas_periodo = resumo_vendas(df_vendas)
