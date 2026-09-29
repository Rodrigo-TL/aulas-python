# QUESTÃO 7: O Desconto da Loja

print("--- QUESTÃO 7: DESCONTO DA LOJA ---")

valor_compra = float(input("Digite o valor total da compra (ex: 250.50): "))

# 15% de desconto é igual a multiplicar por 0.15

desconto = valor_compra * 0.15
valor_final = valor_compra - desconto

print(f"Valor original: R$ {valor_compra:.2f}")
print(f"Valor economizado: R$ {desconto:.2f}")
print(f"Valor final com desconto: R$ {valor_final:.2f}\n")
