# Sistema de Radar de Trânsito

VELOCIDADE_MAXIMA = 80  # km/h

velocidade = float(input("Digite a velocidade atual do carro (em km/h): "))


if velocidade > VELOCIDADE_MAXIMA:
    print("Você foi multado por excesso de velocidade!")

else:
    print("Velocidade dentro do limite permitido. Boa viagem!")
