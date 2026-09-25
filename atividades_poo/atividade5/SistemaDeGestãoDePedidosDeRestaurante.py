class ItemPedido:
    def __init__(self, descricao, valor):
        self.descricao = descricao

        try:
            self.valor = float(valor)
        except ValueError:
            raise ValueError(
                f"Erro: O valor para '{descricao}' deve ser estritamente numérico."
            )


class Mesa:
    def __init__(self, numero_mesa):
        self.numero_mesa = numero_mesa
        self.pedidos = []

    def adicionar_pedido(self, item):
        self.pedidos.append(item)
        print(f"-> {item.descricao} adicionado à {self.numero_mesa}.")

    def somar_total(self):
        return sum(item.valor for item in self.pedidos)

    def fechar_conta(self, taxa_servico):
        subtotal = self.somar_total()
        valor_taxa = subtotal * taxa_servico / 100
        total = subtotal + valor_taxa

        print(f"\nExtrato da {self.numero_mesa}")
        for item in self.pedidos:
            print(f"- {item.descricao}: R$ {item.valor:.2f}")
        print(f"Subtotal: R$ {subtotal:.2f}")
        print(f"Taxa de serviço ({taxa_servico}%): R$ {valor_taxa:.2f}")
        print(f"Total a pagar: R$ {total:.2f}")

        self.pedidos.clear()


def registrar_pedido_seguro(mesa, descricao, valor):
    try:
        item = ItemPedido(descricao, valor)
        mesa.adicionar_pedido(item)
    except ValueError as erro:
        print(f"ALERTA DO SISTEMA: {erro}")


if __name__ == "__main__":
    mesa1 = Mesa("Mesa 1")

    registrar_pedido_seguro(mesa1, "Pizza Margherita", 45.90)
    registrar_pedido_seguro(mesa1, "Refrigerante", 8.50)

    print("\n--- TESTANDO ENTRADA INVÁLIDA ---")
    registrar_pedido_seguro(mesa1, "Pudim", "quinze")
    registrar_pedido_seguro(mesa1, "Café", "5,50")

    registrar_pedido_seguro(mesa1, "Suco de Laranja", 12.00)

    print("\n--- FECHAMENTO DA CONTA ---")
    mesa1.fechar_conta(taxa_servico=10)

    print("\n--- VERIFICANDO STATUS DA MESA APÓS FECHAMENTO ---")
    mesa1.fechar_conta(taxa_servico=10)
