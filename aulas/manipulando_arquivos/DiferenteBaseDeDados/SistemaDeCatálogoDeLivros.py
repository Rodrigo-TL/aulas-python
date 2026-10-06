import json
from pathlib import Path


PASTA_ATIVIDADE = Path(__file__).parent
ARQUIVO_TXT = PASTA_ATIVIDADE / "banco_livros.txt"
ARQUIVO_JSON = PASTA_ATIVIDADE / "catalogo.json"


def ler_banco_legado():
    catalogo_livros = []

    with open(ARQUIVO_TXT, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if not linha:
                continue

            id_livro, nome, descricao, preco, em_estoque = linha.split(";")
            catalogo_livros.append(
                {
                    "id": int(id_livro),
                    "nome": nome,
                    "descricao": descricao,
                    "preco": float(preco),
                    "em_estoque": int(em_estoque),
                }
            )

    return catalogo_livros


def salvar_catalogo(catalogo_livros):
    with open(ARQUIVO_JSON, "w", encoding="utf-8") as arquivo:
        json.dump(catalogo_livros, arquivo, indent=4, ensure_ascii=False)


def ler_catalogo_final():
    with open(ARQUIVO_JSON, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def exibir_resumo(catalogo_livros):
    livros_com_estoque_baixo = [
        livro["nome"]
        for livro in catalogo_livros
        if livro["em_estoque"] < 15
    ]
    valor_total = sum(
        livro["preco"] * livro["em_estoque"] for livro in catalogo_livros
    )

    print("Livros com menos de 15 unidades em estoque:")
    for nome in livros_com_estoque_baixo:
        print(f"- {nome}")
    print(f"\nValor total do estoque: R$ {valor_total:.2f}")


if __name__ == "__main__":
    catalogo_livros = ler_banco_legado()

    novos_livros = [
        {
            "id": 31,
            "nome": "O Nome do Vento",
            "descricao": "Fantasia sobre um músico lendário.",
            "preco": 59.90,
            "em_estoque": 12,
        },
        {
            "id": 32,
            "nome": "A Revolução dos Bichos",
            "descricao": "Sátira política em forma de fábula.",
            "preco": 34.90,
            "em_estoque": 18,
        },
        {
            "id": 33,
            "nome": "O Hobbit",
            "descricao": "A aventura de Bilbo Bolseiro.",
            "preco": 49.90,
            "em_estoque": 9,
        },
        {
            "id": 34,
            "nome": "Capitães da Areia",
            "descricao": "Romance brasileiro sobre jovens de Salvador.",
            "preco": 42.00,
            "em_estoque": 14,
        },
        {
            "id": 35,
            "nome": "A Menina que Roubava Livros",
            "descricao": "Narrativa sobre livros e sobrevivência.",
            "preco": 54.90,
            "em_estoque": 7,
        },
    ]

    catalogo_livros.extend(novos_livros)
    salvar_catalogo(catalogo_livros)
    exibir_resumo(ler_catalogo_final())
