# CLASSE PAI #
# Animal.py

class Animal:
    def __init__(self, idade, tipo, regiao):
        self.idade = idade
        self._tipo = tipo  # Atributo protegido usado pelo Gato
        self.regiao = regiao

    def comer(self):
        print(f"O {self._tipo} está comendo...")

    def dormir(self):
        print(f"O {self._tipo} está dormindo...")

    def mostrarIdade(self):
        print(f"Idade: {self.idade} anos.")
