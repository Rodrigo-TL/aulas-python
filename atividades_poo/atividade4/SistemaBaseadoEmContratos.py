# Tema escolhido: Sistema de Notificações

from abc import ABC, abstractmethod


class Notificacao(ABC):
    def __init__(self, destinatario):
        self.destinatario = destinatario

    def iniciar_processo(self):
        print("Sistema central: operação de notificação iniciada.")

    @abstractmethod
    def enviar(self, destinatario, mensagem):
        pass


class Email(Notificacao):
    def __init__(self):
        super().__init__("cliente@email.com")

    def enviar(self, destinatario, mensagem):
        if "@" not in destinatario:
            print(f"Email não enviado: endereço inválido ({destinatario}).")
            return

        print(f"Email enviado para {destinatario}: {mensagem}")


class SMS(Notificacao):
    def __init__(self):
        super().__init__("11987654321")

    def enviar(self, destinatario, mensagem):
        numero = "".join(caractere for caractere in destinatario if caractere.isdigit())
        if len(numero) < 9:
            print(f"SMS não enviado: número inválido ({destinatario}).")
            return

        print(f"SMS enviado para {destinatario}: {mensagem}")


class PushNotification(Notificacao):
    def __init__(self):
        super().__init__("token-do-dispositivo")

    def enviar(self, destinatario, mensagem):
        if not destinatario:
            print("Push não enviado: token ausente.")
            return

        print(f"Push enviado para o token {destinatario}: {mensagem}")


def processar_lote(lista_de_objetos):
    for item in lista_de_objetos:
        item.iniciar_processo()
        item.enviar(item.destinatario, "Sua solicitação foi processada.")
        print("-" * 30)


if __name__ == "__main__":
    # A linha abaixo gera TypeError por não ser possível instanciar uma classe abstrata.
    # objeto_generico = Notificacao()

    obj1 = Email()
    obj2 = SMS()
    obj3 = PushNotification()

    lote = [obj1, obj2, obj3, obj1]

    print("\n--- INICIANDO PROCESSAMENTO EM LOTE ---")
    processar_lote(lote)
