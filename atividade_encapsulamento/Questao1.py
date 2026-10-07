import json
from pathlib import Path

ARQUIVO_ESTOQUE = Path(__file__).with_name("estoque.json")


def salvar_estoque(dados):
    with open(ARQUIVO_ESTOQUE, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)


def carregar_estoque():
    with open(ARQUIVO_ESTOQUE, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def exibir_produtos(dados):
    print(f"\n>> STATUS DO ESTOQUE - LOJA: {dados['nome']} <<")
    for produto in dados["produtos"]:
        print(
            f"  * {produto['nome']}: R$ {produto['preco']:.2f} [Qtd: {produto['quantidade']}]"
        )
    print("=" * 40)


loja_inicial = {
    "nome": "TechStore",
    "produtos": [
        {"nome": "Teclado", "preco": 150.00, "quantidade": 12},
        {"nome": "Mouse", "preco": 80.00, "quantidade": 20},
        {"nome": "Monitor", "preco": 899.90, "quantidade": 6},
    ],
}

salvar_estoque(loja_inicial)

dados_lidos = carregar_estoque()

exibir_produtos(dados_lidos)

dados_lidos["produtos"][0]["preco"] *= 0.90

novo_produto = {"nome": "Fone de ouvido", "preco": 199.90, "quantidade": 10}

ja_existe = any(p["nome"] == novo_produto["nome"] for p in dados_lidos["produtos"])
if not ja_existe:
    dados_lidos["produtos"].append(novo_produto)

salvar_estoque(dados_lidos)
