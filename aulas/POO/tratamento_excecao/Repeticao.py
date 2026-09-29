while True:
    valor = ""
    try:
        valor = int(input("Digite a senha: "))
        # Verifica a senha logo após uma digitação válida
        if valor == 1234:
            break
    except ValueError:
        print("Por favor, digite apenas números!")
    except Exception as erro:
        print(f"Erro inesperado: {erro}")
    finally:
        # O finally serve para limpezas ou avisos gerais, pois roda SEMPRE
        print("Tentativa processada.")
