import streamlit as st
import pandas as pd
from data_manipulation import carregar_dados
from data_visualization import grafico_barras_vendas, grafico_linhas_vendas

# --- Título do Dashboard ---
st.set_page_config(page_title="Dashboard de Vendas", layout="wide")
st.title("Dashboard de Vendas - AdventureWorks2022")

# --- Carrega os dados ---
df_vendas = carregar_dados()

# --- Filtros interativos ---
st.sidebar.header("Filtros")

# Filtro por período
data_min = df_vendas["OrderDate"].min()
data_max = df_vendas["OrderDate"].max()
date_range = st.sidebar.date_input(
    "Período do Pedido",
    value=[data_min, data_max],
    min_value=data_min,
    max_value=data_max
)

# Filtro por produto
produtos = df_vendas["ProductName"].unique()
produtos_selecionados = st.sidebar.multiselect("Produtos", produtos, default=produtos)

# Filtro por região
regioes = df_vendas["Region"].unique()
regioes_selecionadas = st.sidebar.multiselect("Regiões", regioes, default=regioes)

# --- Aplica filtros ---
df_filtrado = df_vendas[
    (df_vendas["OrderDate"].dt.date >= date_range[0]) &
    (df_vendas["OrderDate"].dt.date <= date_range[1]) &
    (df_vendas["ProductName"].isin(produtos_selecionados)) &
    (df_vendas["Region"].isin(regioes_selecionadas))
]

# --- KPI ---
total_vendas = df_filtrado["TotalDue"].sum()
st.metric(label="Total de Vendas no Período Filtrado", value=f"${total_vendas:,.2f}")

# --- Gráficos ---
st.subheader("Vendas por Produto")
fig_barras = grafico_barras_vendas(df_filtrado)
st.plotly_chart(fig_barras, use_container_width=True)

st.subheader("Vendas ao Longo do Tempo")
fig_linhas = grafico_linhas_vendas(df_filtrado)
st.plotly_chart(fig_linhas, use_container_width=True)