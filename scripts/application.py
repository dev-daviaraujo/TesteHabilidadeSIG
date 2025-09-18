import pyodbc

# Configurações da conexão
server = 'localhost\SQLEXPRESS'            
database = 'AdventureWorks2022'
driver = 'ODBC Driver 17 for SQL Server'

# String de conexão
conn_str = (
    f'DRIVER={{{driver}}};'
    f'SERVER={server};'
    f'DATABASE={database};'
    'Trusted_Connection=yes;'       # Windows Authentication
    'TrustServerCertificate=yes;'   # evita erro SSL
)

# Conectando ao banco
try:
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    
except Exception as e:
    print("Erro ao conectar:", e)
finally:
    if 'conn' in locals():
        conn.close()
