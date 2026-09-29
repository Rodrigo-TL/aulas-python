# Questão 8: A Calculadora de Lucro da Empresa

print("--- Questão 8 ---")

nome_produto = input("Digite o nome do produto: ")
custo_fabrica = float(input("Digite o custo de fábrica do produto: "))
preco_venda = float(input("Digite o preço de venda na loja: "))

lucro = preco_venda - custo_fabrica
lucro_bom = lucro > 20.00

print(f"Produto: {nome_produto}")
print(f"Lucro obtido: R$ {lucro:.2f}")
print(f"O lucro foi bom? {lucro_bom}")