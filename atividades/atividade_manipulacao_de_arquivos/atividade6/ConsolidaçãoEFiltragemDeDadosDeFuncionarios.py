import json
from pathlib import Path


PASTA_ATIVIDADE = Path(__file__).parent


def ler_base(nome_arquivo):
    caminho = PASTA_ATIVIDADE / nome_arquivo

    with open(caminho, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def consolidar_aniversariantes():
    dados1 = ler_base("base1.json")
    dados2 = ler_base("base2.json")
    dados3 = ler_base("base3.json")

    lista_aniversariantes = []

    for dados in (dados1, dados2, dados3):
        for funcionario in dados:
            aniversariante = {
                "nome": funcionario["nome"],
                "aniversario": funcionario["aniversario"]
            }
            lista_aniversariantes.append(aniversariante)

    lista_aniversariantes.sort(key=lambda funcionario: funcionario["nome"])

    caminho_saida = PASTA_ATIVIDADE / "aniversariantes.json"

    with open(caminho_saida, "w", encoding="utf-8") as arquivo:
        json.dump(
            lista_aniversariantes,
            arquivo,
            indent=4,
            ensure_ascii=False
        )

    print(
        f"{len(lista_aniversariantes)} registros processados com sucesso."
    )


if __name__ == "__main__":
    consolidar_aniversariantes()