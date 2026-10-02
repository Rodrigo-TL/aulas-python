from pathlib import Path


ARQUIVO_ALUNOS = Path(__file__).with_name("alunos.txt")


def ler_alunos():
    alunos = []

    try:
        with open(ARQUIVO_ALUNOS, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if linha:
                    alunos.append(linha.split(";"))
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {ARQUIVO_ALUNOS.name}")

    return alunos


def encontrar_aluno(nome):
    nome_pesquisado = nome.strip().casefold()
    for aluno in ler_alunos():
        if aluno[0].casefold() == nome_pesquisado:
            return aluno
    raise ValueError(f"Aluno não encontrado: {nome}")


def calcular_media(aluno):
    notas = [float(nota.replace(",", ".")) for nota in aluno[2:6]]
    return sum(notas) / len(notas)


def acrescentar_aluno():
    nome = input("Nome do aluno: ").strip()
    turma = input("Turma: ").strip()
    notas = []

    for numero in range(1, 5):
        while True:
            try:
                nota = float(
                    input(f"Nota do {numero}º bimestre: ").replace(",", ".")
                )
                if not 0 <= nota <= 10:
                    raise ValueError
                notas.append(nota)
                break
            except ValueError:
                print("Digite uma nota numérica entre 0 e 10.")

    media = sum(notas) / 4
    status = "Aprovado" if media >= 7 else "Reprovado"
    registro = (
        f"{nome};{turma};"
        f"{notas[0]:.1f};{notas[1]:.1f};"
        f"{notas[2]:.1f};{notas[3]:.1f};{status}\n"
    )

    with open(ARQUIVO_ALUNOS, "a", encoding="utf-8") as arquivo:
        arquivo.write(registro)

    print(f"Aluno {nome} adicionado com status: {status}.")


def mostrar_media():
    nome = input("Nome do aluno: ")
    try:
        aluno = encontrar_aluno(nome)
        print(f"A média de {aluno[0]} é {calcular_media(aluno):.2f}.")
    except (ValueError, FileNotFoundError) as erro:
        print(f"Erro: {erro}")


def consultar_status():
    nome = input("Nome do aluno: ")
    try:
        aluno = encontrar_aluno(nome)
        print(f"{aluno[0]} está {aluno[6]}.")
    except (ValueError, FileNotFoundError) as erro:
        print(f"Erro: {erro}")


def mostrar_maior_media():
    turma = input("Turma: ").strip()
    alunos_turma = [aluno for aluno in ler_alunos() if aluno[1] == turma]

    if not alunos_turma:
        print(f"Nenhum aluno encontrado na turma {turma}.")
        return

    aluno = max(alunos_turma, key=calcular_media)
    print(
        f"Maior média da turma {turma}: "
        f"{aluno[0]} ({calcular_media(aluno):.2f})."
    )


def exibir_menu():
    print("\n--- SISTEMA DE GESTÃO ESCOLAR ---")
    print("1 - Acrescentar um aluno")
    print("2 - Calcular média de um aluno")
    print("3 - Consultar status de aprovação")
    print("4 - Mostrar maior média da turma")
    print("5 - Sair")


def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            acrescentar_aluno()
        elif opcao == "2":
            mostrar_media()
        elif opcao == "3":
            consultar_status()
        elif opcao == "4":
            mostrar_maior_media()
        elif opcao == "5":
            print("Sistema encerrado.")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
