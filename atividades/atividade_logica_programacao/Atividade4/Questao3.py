# Validador de Idade para Votação

IDADE_MINIMA_VOTO = 18

idade = int(input("Digite sua idade: "))

if idade >= IDADE_MINIMA_VOTO:
    print("Você é obrigado a votar")

else:
    print("Você ainda não é obrigado a votar")
