# Simulador de Saque Bancário

saldo_atual = float(input("Digite o saldo atual da conta (R$): "))

valor_saque = float(input("Digite o valor que deseja sacar (R$): "))

# Verificar se o saque é possível
if valor_saque <= saldo_atual:
    saldo_atual -= valor_saque
    print(f"Saque realizado com sucesso! Saldo atual: R$ {saldo_atual:.2f}")

else:
    print("Saldo insuficiente para realizar esta operação")
