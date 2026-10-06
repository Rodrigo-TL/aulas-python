import json
from pathlib import Path


ARQUIVO_ESTOQUE = Path(__file__).with_name("estoque.json")


loja = {
    "nome": "TechStore",
    "produtos": [
        {"nome": "Teclado", "preco": 150.00, "quantidade": 12},
        {"nome": "Mouse", "preco": 80.00, "quantidade": 20},
        {"nome": "Monitor", "preco": 899.90, "quantidade": 6},
    ],
}


with open(ARQUIVO_ESTOQUE, "w", encoding="utf-8") as arquivo:
    json.dump(loja, arquivo, indent=4, ensure_ascii=False)


with open(ARQUIVO_ESTOQUE, "r", encoding="utf-8") as arquivo:
    dados_lidos = json.load(arquivo)


for produto in dados_lidos["produtos"]:
    print(f"O produto {produto['nome']} custa R$ {produto['preco']:.2f}")


dados_lidos["produtos"][0]["preco"] *= 0.90
dados_lidos["produtos"].append(
    {"nome": "Fone de ouvido", "preco": 199.90, "quantidade": 10}
)


with open(ARQUIVO_ESTOQUE, "w", encoding="utf-8") as arquivo:
    json.dump(dados_lidos, arquivo, indent=4, ensure_ascii=False)

