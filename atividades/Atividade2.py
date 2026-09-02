# Coleta dos dados do usuário

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

# O usuário digita True ou False, e convertemos para booleano comparando a string
tem_plano = input("Tem plano de saúde? (True/False): ").strip().lower() == 'true'

# Regra de negócio: menor de idade (< 18), idoso (>= 60) ou sem plano de saúde (False) não é aceito
aceito = not (idade < 18 or idade >= 60 or not tem_plano)

# Retorno das informações em um único print()
print(f"Seu nome é {nome}, você tem {idade} anos. Tem plano? {tem_plano}. Você foi aceito? {aceito}.")
