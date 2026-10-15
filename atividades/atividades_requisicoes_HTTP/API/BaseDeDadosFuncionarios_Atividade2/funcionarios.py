import json

import requests


link_funcionarios = "http://192.168.205.100:8080/funcionarios"
arquivo_saida = "dados_funcionarios_atualizados.json"


def campo_vazio(valor):
    return valor is None or (
        isinstance(valor, str) and valor.strip() == ""
    )


def consultar_cep(cep):
    """Consulta o CEP e aceita somente retornos com cidade e estado."""
    cep = cep.strip().replace("-", "")

    if not cep.isdigit() or len(cep) != 8:
        raise ValueError("O CEP deve conter exatamente 8 números.")

    link_cep = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(link_cep, timeout=10)
    resposta.raise_for_status()
    endereco = resposta.json()

    if (
        endereco.get("erro")
        or not endereco.get("localidade")
        or not endereco.get("uf")
    ):
        raise ValueError(
            "O CEP não foi encontrado ou não possui endereço válido."
        )

    return cep, endereco


def solicitar_cep(nome):
    """Solicita novamente até que o usuário informe um CEP válido."""
    while True:
        cep_digitado = input(
            f"Digite um CEP válido para {nome}: "
        )

        try:
            return consultar_cep(cep_digitado)
        except (ValueError, requests.RequestException) as erro:
            print(f"CEP inválido: {erro}")


def preencher_dados_vazios(funcionario, endereco):
    """Preenche somente os campos que estão vazios."""
    dados_endereco = {
        "cidade": endereco.get("localidade"),
        "estado": endereco.get("uf"),
        "logradouro": endereco.get("logradouro"),
        "bairro": endereco.get("bairro"),
        "complemento": endereco.get("complemento"),
    }

    for campo, valor in dados_endereco.items():
        if campo in funcionario and campo_vazio(funcionario[campo]):
            funcionario[campo] = valor


def atualizar_funcionarios():
    resposta = requests.get(link_funcionarios, timeout=10)
    resposta.raise_for_status()
    lista_funcionarios = resposta.json()

    if not isinstance(lista_funcionarios, list):
        raise ValueError(
            "A API deve retornar uma lista de funcionários."
        )

    print("--- FUNCIONÁRIOS COM DADOS DE ENDEREÇO VAZIOS ---\n")

    for funcionario in lista_funcionarios:
        nome = funcionario.get("nome", "funcionário")
        cep = funcionario.get("cep")

        campos_endereco = (
            "cidade",
            "estado",
            "logradouro",
            "bairro",
        )

        possui_dado_vazio = any(
            campo_vazio(funcionario.get(campo))
            for campo in campos_endereco
        )

        if not campo_vazio(cep) and not possui_dado_vazio:
            continue

        if campo_vazio(cep):
            print(
                f"O funcionário(a) {nome} não tem CEP cadastrado."
            )

            cep, endereco = solicitar_cep(nome)
            funcionario["cep"] = cep
            preencher_dados_vazios(funcionario, endereco)
            continue

        try:
            cep, endereco = consultar_cep(str(cep))
            funcionario["cep"] = cep
            preencher_dados_vazios(funcionario, endereco)

        except (ValueError, requests.RequestException) as erro:
            print(
                f"Não foi possível consultar o CEP de {nome}: {erro}"
            )

    return lista_funcionarios


def salvar_dados(lista_funcionarios):
    with open(arquivo_saida, "w", encoding="utf-8") as arquivo:
        json.dump(
            lista_funcionarios,
            arquivo,
            indent=4,
            ensure_ascii=False,
        )


def main():
    try:
        lista_funcionarios = atualizar_funcionarios()

        print("\n--- BASE DE DADOS ATUALIZADA ---\n")

        for funcionario in lista_funcionarios:
            print(funcionario)

        salvar_dados(lista_funcionarios)

        print(f"\nArquivo salvo como: {arquivo_saida}")

    except (
        OSError,
        ValueError,
        requests.RequestException,
        json.JSONDecodeError,
    ) as erro:
        print(f"Não foi possível atualizar os dados: {erro}")


if __name__ == "__main__":
    main()