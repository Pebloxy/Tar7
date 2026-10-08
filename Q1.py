# -*- coding: utf-8 -*-

valor = 0
dias = 0
txMulta = 0.02
txJuros = 0.01
multa = 0
juros = 0
valorPagar = 0

while True:

    print("\n===== MENU =====")
    print("1 - Leitura")
    print("2 - Cálculo")
    print("3 - Impressão")
    print("4 - Saída")

    opcao = int(input("Digite uma opção: "))

    if opcao == 1:

        valor = float(input("Digite o valor da prestação: "))
        dias = int(input("Digite a quantidade de dias em atraso: "))

    elif opcao == 2:

        multa = txMulta * valor
        juros = txJuros * (1 / 30) * dias * valor
        valorPagar = valor + multa + juros

        print("Cálculo realizado!")

    elif opcao == 3:

        print("\nValor:", valor)
        print("Dias:", dias)
        print("Multa:", multa)
        print("Juros:", juros)
        print("Valor a pagar:", valorPagar)

    elif opcao == 4:

        print("Programa encerrado.")
        break

    else:

        print("Opção inválida!")