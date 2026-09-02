
# QUESTÃO 2: A Média do Semestre

print("--- QUESTÃO 2: MÉDIA DO SEMESTRE ---")
nome_aluno = input("Digite o seu nome: ")
nota1 = float(input("Digite a nota da 1ª prova: "))
nota2 = float(input("Digite a nota da 2ª prova: "))
nota3 = float(input("Digite a nota da 3ª prova: "))

# Parênteses garantem que a soma seja feita antes da divisão
media_final = (nota1 + nota2 + nota3) / 3

print(f"Olá {nome_aluno}, a sua média final foi de {media_final:.2f}\n")



# QUESTÃO 5: Sistema de Cálculo de Idade

print("--- QUESTÃO 5: CÁLCULO DE IDADE ---")
ano_nascimento = int(input("Digite o seu ano de nascimento: "))
ano_atual = int(input("Digite o ano em que estamos: "))

idade = ano_atual - ano_nascimento

print(f"Sua idade é ou será de: {idade} anos.\n")


# QUESTÃO 6: Trocando os Valores

print("--- QUESTÃO 6: TROCA DE VALORES ---")
X = 15
Y = 30

# Lógica usando o copo reserva (variável auxiliar) para inverter os valores
reserva = X
X = Y
Y = reserva

print("Valor final de X (deve ser 30):", X)
print("Valor final de Y (deve ser 15):", Y)
print()


# QUESTÃO 7: O Desconto da Loja

print("--- QUESTÃO 7: DESCONTO DA LOJA ---")
valor_compra = float(input("Digite o valor total da compra (ex: 250.50): "))

# 15% de desconto é igual a multiplicar por 0.15
desconto = valor_compra * 0.15
valor_final = valor_compra - desconto

print(f"Valor original: R$ {valor_compra:.2f}")
print(f"Valor economizado: R$ {desconto:.2f}")
print(f"Valor final com desconto: R$ {valor_final:.2f}\n")


# QUESTÃO 8: Prova Real dos Tipos de Dados

print("--- QUESTÃO 8: PROVA REAL DOS TIPOS ---")
# Fazendo o casting (conversão) direto em cada entrada
nome_user = str(input("Digite seu Nome: "))
idade_user = int(input("Digite sua Idade: "))
altura_user = float(input("Digite sua Altura (ex: 1.75): "))

print("\nComprovação dos tipos de dados:")
print("Variável nome_user é:", type(nome_user))
print("Variável idade_user é:", type(idade_user))
print("Variável altura_user é:", type(altura_user))
