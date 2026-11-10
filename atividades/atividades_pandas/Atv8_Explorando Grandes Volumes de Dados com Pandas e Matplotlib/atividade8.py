from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd


PASTA_ATIVIDADE = Path(__file__).resolve().parent
ARQUIVO_CSV = PASTA_ATIVIDADE / "customers-10000.csv"

df = pd.read_csv(ARQUIVO_CSV)
df["Subscription Date"] = pd.to_datetime(
    df["Subscription Date"], errors="coerce"
)

if df["Subscription Date"].isna().any():
    raise ValueError("A base contém datas de assinatura inválidas.")

# A base não tem coluna de status; cada registro é contado como assinatura cadastrada.
assinaturas_por_pais = df["Country"].value_counts()
assinaturas_por_cidade = df["City"].value_counts()
assinaturas_por_empresa = df["Company"].value_counts()

print(f"Total de registros: {len(df):,}")
print(
    "Período coberto: "
    f"{df['Subscription Date'].min():%d/%m/%Y} a "
    f"{df['Subscription Date'].max():%d/%m/%Y}"
)
print("\nPaís com mais registros:")
print(assinaturas_por_pais.head(1).to_string())

maior_quantidade_cidade = assinaturas_por_cidade.max()
cidades_lideres = assinaturas_por_cidade[
    assinaturas_por_cidade == maior_quantidade_cidade
]
print(
    f"\nCidades líderes empatadas ({maior_quantidade_cidade} registros cada):"
)
print(cidades_lideres.to_string())

print("\nCinco empresas com mais registros:")
print(assinaturas_por_empresa.sort_values(ascending=False).head(5).to_string())
print(
    "Empresas empatadas no máximo: "
    f"{(assinaturas_por_empresa == assinaturas_por_empresa.max()).sum()}"
)

# Gráfico 1: dez países com mais registros.
top_paises = assinaturas_por_pais.head(10).sort_values()
fig, ax = plt.subplots(figsize=(10, 6))
top_paises.plot(kind="barh", ax=ax, color="#4e79a7")
ax.set_title("Top 10 países por número de assinaturas cadastradas")
ax.set_xlabel("Número de registros")
ax.set_ylabel("País")
ax.grid(axis="x", alpha=0.25)
plt.tight_layout()
plt.savefig(
    PASTA_ATIVIDADE / "grafico_1_top_10_paises.png",
    dpi=150,
    bbox_inches="tight",
)
plt.close()

# Gráfico 2: evolução mensal; 2022 é parcial na base (até maio).
assinaturas_por_mes = (
    df.set_index("Subscription Date")
    .resample("MS")
    .size()
)
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(
    assinaturas_por_mes.index,
    assinaturas_por_mes.values,
    marker="o",
    linewidth=1.8,
    color="#e15759",
)
ax.set_title("Evolução mensal das assinaturas cadastradas")
ax.set_xlabel("Mês")
ax.set_ylabel("Número de registros")
ax.grid(alpha=0.25)
fig.autofmt_xdate()
plt.tight_layout()
plt.savefig(
    PASTA_ATIVIDADE / "grafico_2_evolucao_mensal.png",
    dpi=150,
    bbox_inches="tight",
)
plt.close()

print("\nGráficos salvos na pasta da atividade:")
print("- grafico_1_top_10_paises.png")
print("- grafico_2_evolucao_mensal.png")
