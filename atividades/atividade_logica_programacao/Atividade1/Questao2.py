
# QUESTÃO 2: A Média do Semestre

print("--- QUESTÃO 2: MÉDIA DO SEMESTRE ---")

nome_aluno = input("Digite o seu nome: ")
nota1 = float(input("Digite a nota da 1ª prova: "))
nota2 = float(input("Digite a nota da 2ª prova: "))
nota3 = float(input("Digite a nota da 3ª prova: "))

# Parênteses garantem que a soma seja feita antes da divisão

media_final = (nota1 + nota2 + nota3) / 3

print(f"Olá {nome_aluno}, a sua média final foi de {media_final:.2f}\n")
