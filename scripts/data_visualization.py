import pandas as pd
import plotly.express as px

def grafico_barras_vendas(df: pd.DataFrame, produto_col="ProductName", valor_col="TotalDue") -> px.bar:
    """Cria gráfico de barras mostrando vendas por produto.
    
    Argumentos:
        df: DataFrame contendo os dados.
        produto_col: nome da coluna com os produtos.
        valor_col: nome da coluna com o valor total.    
    Retorno:
        fig_barras: figura Plotly
    """
    vendas_produto = df.groupby(produto_col)[valor_col].sum().reset_index()
    
    # Definindo parâmetros do gráfico de barras
    fig_barras = px.bar(
        vendas_produto,
        x=produto_col,
        y=valor_col,
        title="Vendas por Produto",
        labels={valor_col: "Valor Total", produto_col: "Produto"}
    )
    
    return fig_barras


def grafico_linhas_vendas(df: pd.DataFrame, data_col="OrderDate", valor_col="TotalDue") -> px.line:
    """Cria gráfico de linhas mostrando vendas ao longo do tempo (ano-mês).
    
    Args:
        df: DataFrame contendo os dados.
        data_col: nome da coluna com a data do pedido.
        valor_col: nome da coluna com o valor total.    
    Returns:
        fig_linhas: figura Plotly
    """
    # Cria coluna ano-mês
    df["ano_mes"] = df[data_col].dt.to_period("M").astype(str)
    
    vendas_tempo = df.groupby("ano_mes")[valor_col].sum().reset_index()
    
    # Definindo parâmetros do gráfico de linhas
    fig_linhas = px.line(
        vendas_tempo,
        x="ano_mes",
        y=valor_col,
        title="Vendas ao Longo do Tempo",
        labels={valor_col: "Valor Total", "ano_mes": "Ano-Mês"}
    )
    
    return fig_linhas


if __name__ == "__main__":
    # Carrega os dados do SQL Server
    from data_manipulation import carregar_dados
    df_vendas = carregar_dados()

    # Cria gráficos com Plotly
    fig_barras = grafico_barras_vendas(df_vendas)
    fig_linhas = grafico_linhas_vendas(df_vendas)

    # Para exibir o gráfico no navegador basta retirar o # da linha com o gráfico que deseja exibir
    #fig_barras.show()
    #fig_linhas.show()
    
