from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd


PASTA_ATIVIDADE = Path(__file__).resolve().parent
ARQUIVO_CSV = PASTA_ATIVIDADE / "alunos_senai_sig.csv"

df = pd.read_csv(ARQUIVO_CSV)
df["Media_Final"] = pd.to_numeric(df["Media_Final"], errors="raise")

# Gráfico 1: menor e maior média de cada curso.
extremos = df.groupby("Curso")["Media_Final"].agg(["min", "max"]).sort_index()
ax = extremos.plot(
    kind="bar",
    figsize=(10, 6),
    color=["#f28e2b", "#4e79a7"],
    edgecolor="black",
)
ax.set_title("Menores e maiores médias por curso")
ax.set_xlabel("Curso")
ax.set_ylabel("Média final")
ax.set_ylim(0, 10.8)
ax.legend(["Menor média", "Maior média"])
ax.tick_params(axis="x", rotation=0)
ax.grid(axis="y", alpha=0.25)
plt.tight_layout()
plt.savefig(PASTA_ATIVIDADE / "grafico_1_medias_por_curso.png", dpi=150)
plt.close()

# Gráfico 2: notas de Design e Java por ordem dos alunos na base.
cursos_plot = ["Design", "Java"]
dados_plot = df[df["Curso"].isin(cursos_plot)].copy()
dados_plot["Ordem"] = dados_plot.groupby("Curso").cumcount() + 1
maiores_notas = df.nlargest(2, "Media_Final")

fig, ax = plt.subplots(figsize=(11, 6))
cores = {"Design": "#e15759", "Java": "#4e79a7"}
for curso in cursos_plot:
    dados_curso = dados_plot[dados_plot["Curso"] == curso]
    ax.plot(
        dados_curso["Ordem"],
        dados_curso["Media_Final"],
        marker="o",
        linewidth=2,
        label=curso,
        color=cores[curso],
    )

for _, aluno in maiores_notas.iterrows():
    if aluno["Curso"] not in cursos_plot:
        continue
    linha = dados_plot[
        (dados_plot["Curso"] == aluno["Curso"])
        & (dados_plot["Nome"] == aluno["Nome"])
    ].iloc[0]
    ax.scatter(
        linha["Ordem"],
        aluno["Media_Final"],
        marker="*",
        s=220,
        color="#f1c40f",
        edgecolor="black",
        zorder=5,
    )
    ax.annotate(
        "maior nota",
        (linha["Ordem"], aluno["Media_Final"]),
        xytext=(0, 12),
        textcoords="offset points",
        ha="center",
        fontsize=9,
        fontweight="bold",
    )

ax.set_title("Notas dos alunos de Design e Java")
ax.set_xlabel("Aluno (ordem no arquivo)")
ax.set_ylabel("Média final")
ax.set_xticks(range(1, dados_plot["Ordem"].max() + 1))
ax.set_ylim(0, 11)
ax.legend(title="Curso")
ax.grid(alpha=0.25)
plt.tight_layout()
plt.savefig(PASTA_ATIVIDADE / "grafico_2_notas_design_java.png", dpi=150)
plt.close()

# Gráfico 3: aprovação em Python considerando média mínima 7.
alunos_python = df[df["Curso"] == "Python"]
aprovados = int((alunos_python["Media_Final"] >= 7).sum())
reprovados = int((alunos_python["Media_Final"] < 7).sum())

fig, ax = plt.subplots(figsize=(7, 7))
ax.pie(
    [aprovados, reprovados],
    labels=[f"Aprovados ({aprovados})", f"Reprovados ({reprovados})"],
    autopct="%1.1f%%",
    startangle=90,
    colors=["#59a14f", "#e15759"],
    wedgeprops={"edgecolor": "white"},
)
ax.set_title("Aprovação no curso de Python (média mínima 7)")
ax.axis("equal")
plt.tight_layout()
plt.savefig(PASTA_ATIVIDADE / "grafico_3_aprovacao_python.png", dpi=150)
plt.close()

print("Gráficos salvos na pasta da atividade:")
print("- grafico_1_medias_por_curso.png")
print("- grafico_2_notas_design_java.png")
print("- grafico_3_aprovacao_python.png")
print(f"Aprovação em Python: {aprovados} aprovados, {reprovados} reprovados.")
