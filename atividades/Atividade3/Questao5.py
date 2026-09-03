# Questão 5: O Sistema de Desconto (Lógica OR)

print("--- Questão 5 ---")

valor_compra = float(input("Digite o valor total da compra: "))
eh_vip = int(input("Você possui cartão VIP? (Digite 1 para Sim ou 0 para Não): "))

# Converte o input numérico para um booleano (1 vira True, 0 vira False)

tem_cartao_vip = eh_vip == 1

frete_gratis = (valor_compra > 200.00) or tem_cartao_vip

print(f"Tem direito a frete grátis? {frete_gratis}\n")