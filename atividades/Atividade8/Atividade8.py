#  Média Final do Aluno

def avaliar_aluno(nome, primeiro_bimestre, segundo_bimestre, terceiro_bimestre, quarto_bimestre):
    media_final = (
        primeiro_bimestre
        + segundo_bimestre
        + terceiro_bimestre
        + quarto_bimestre
    ) / 4

    print(f"\nAluno: {nome}")
    print(f"Nota do 1º bimestre: {primeiro_bimestre:.2f}")
    print(f"Nota do 2º bimestre: {segundo_bimestre:.2f}")
    print(f"Nota do 3º bimestre: {terceiro_bimestre:.2f}")
    print(f"Nota do 4º bimestre: {quarto_bimestre:.2f}")
    print(f"Média final: {media_final:.2f}")

    if media_final >= 7:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")


nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a nota do 1º bimestre: "))
nota2 = float(input("Digite a nota do 2º bimestre: "))
nota3 = float(input("Digite a nota do 3º bimestre: "))
nota4 = float(input("Digite a nota do 4º bimestre: "))

avaliar_aluno(nome, nota1, nota2, nota3, nota4)
