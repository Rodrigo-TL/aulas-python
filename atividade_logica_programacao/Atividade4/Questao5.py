# Catraca VIP de Eventos

# Solicitar informações do convidado
idade = int(input("Digite sua idade: "))
convite_vip = int(input("Possui convite VIP? (1 para Sim, 0 para Não): "))
organizador = int(input("É organizador do evento? (1 para Sim, 0 para Não): "))

# Validar acesso com combinação de AND e OR
if (idade >= 18 and convite_vip == 1) or organizador == 1:
    print("Entrada PERMITIDA! Seja bem-vindo(a)")

else:
    print("Entrada NEGADA! Você não atende aos requisitos")
