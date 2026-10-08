import json
from pathlib import Path


ARQUIVO_ESTOQUE = Path(__file__).with_name("estoque.json")


loja = {
    "nome": "TechStore",
    "produtos": [
        {
            "nome": "Teclado",
            "preco": 150.00,
            "quantidade": 12
        },
        {
            "nome": "Mouse",
            "preco": 80.00,
            "quantidade": 20
        },
        {
            "nome": "Monitor",
            "preco": 899.90,
            "quantidade": 6
        }
    ]
}


# Parte 1: salvando os dados iniciais
with open(ARQUIVO_ESTOQUE, "w", encoding="utf-8") as arquivo:
    json.dump(
        loja,
        arquivo,
        indent=4,
        ensure_ascii=False
    )


# Parte 2: lendo os dados salvos
with open(ARQUIVO_ESTOQUE, "r", encoding="utf-8") as arquivo:
    dados_lidos = json.load(arquivo)


# Exibindo nome e preço dos produtos
for produto in dados_lidos["produtos"]:
    print(
        f"O produto {produto['nome']} "
        f"custa R$ {produto['preco']:.2f}"
    )


# Desafio extra: aplicando desconto de 10% no Teclado
dados_lidos["produtos"][0]["preco"] *= 0.90


# Adicionando um novo produto
novo_produto = {
    "nome": "Fone de ouvido",
    "preco": 199.90,
    "quantidade": 10
}

dados_lidos["produtos"].append(novo_produto)


# Salvando novamente o arquivo atualizado
with open(ARQUIVO_ESTOQUE, "w", encoding="utf-8") as arquivo:
    json.dump(
        dados_lidos,
        arquivo,
        indent=4,
        ensure_ascii=False
    )