class Pessoa:
    #Construtor e atributos
    def __init__(self, nome, idade, profissao, cidade, email):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
        self.cidade = cidade
        self.email = email
    #Metodo converncional apresentar
    def apresentar(self):
        return f"{self.nome}, {self.idade} anos, {self.profissao} de {self.cidade}."

    # Metodo converncional idade
    def fazer_aniversario(self):
        self.idade += 1

    # Metodo converncional e-mail
    def atualizar_email(self, novo_email):
        self.email = novo_email

    # 5 Objetos criados na lista Pessoas
pessoas = [
    Pessoa("Ana", 28, "Engenheira", "São Paulo", "ana@email.com"),
    Pessoa("Bruno", 35, "Professor", "Curitiba", "bruno@email.com"),
    Pessoa("Carla", 22, "Designer", "Recife", "carla@email.com"),
    Pessoa("Celso", 60, "Astronauta", "Goiania", "celsoromao@email.com"),
    Pessoa("Elisa", 30, "Jornalista", "Porto Alegre", "elisa@email.com"),
]

pessoas[0].fazer_aniversario()
pessoas[1].atualizar_email("bruno.novo@email.com")

for pessoa in pessoas:
    print(
        f"{pessoa.apresentar()} "
        f"E-mail: {pessoa.email}"
    )