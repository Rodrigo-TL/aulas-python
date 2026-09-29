usuario = input("Digite seu nome para iniciar a compra: ")

carrinho = []
total = 0

while True:
    nome_produto = input(
        "\nDigite 'fim' para finalizar.\n"
        "Digite o nome do produto: "
    )

    if nome_produto.lower() == "fim":
        break

    try:
        preco_produto = float(
            input("Digite o valor desse produto: ").replace(",", ".")
        )
    except ValueError:
        print("Valor inválido. Digite apenas números.")
        continue

    carrinho.append([nome_produto, preco_produto])
    total += preco_produto


print("\n--- FINALIZANDO COMPRA ---")

with open("pagamento.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("RECIBO DO CARRINHO\n\n")
    arquivo.write(f"Cliente: {usuario}\n\n")

    for produto in carrinho:
        nome_produto = produto[0]
        preco_produto = produto[1]

        arquivo.write(
            f"Produto: {nome_produto} - "
            f"R$ {preco_produto:.2f}\n"
        )

    arquivo.write(f"\nTOTAL: R$ {total:.2f}\n")


print("\n--- PROCESSANDO PAGAMENTO ---")

with open("pagamento.txt", "r", encoding="utf-8") as arquivo:
    recibo = arquivo.read()

marcador = "TOTAL: R$ "
inicio_total = recibo.find(marcador)

if inicio_total != -1:
    inicio_valor = inicio_total + len(marcador)
    fim_valor = recibo.find("\n", inicio_valor)

    valor_total = recibo[inicio_valor:fim_valor]

    print(
        f"Compra processada com sucesso! "
        f"Valor cobrado: R$ {valor_total}"
    )
else:
    print("Erro: valor total não encontrado no recibo.")