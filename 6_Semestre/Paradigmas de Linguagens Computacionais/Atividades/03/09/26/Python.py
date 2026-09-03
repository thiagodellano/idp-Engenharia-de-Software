while True:

    print("\n--- CALCULADORA ---")
    print("1 - Soma")
    print("2 - Multiplicacao")
    print("3 - Divisao")
    print("4 - Subtracao")
    print("5 - Elevar ao quadrado")
    print("6 - Exponencial")
    print("7 - Taylor Exponencial")
    print("8 - Taylor Seno")
    print("0 - Sair")

    opcao = int(input("Escolha: "))

    if opcao == 1:

        a = float(input("Digite o primeiro numero: "))
        b = float(input("Digite o segundo numero: "))

        resultado = a + b

        print("Resultado:", resultado)

    elif opcao == 2:

        a = float(input("Digite o primeiro numero: "))
        b = float(input("Digite o segundo numero: "))

        resultado = a * b

        print("Resultado:", resultado)

    elif opcao == 3:

        a = float(input("Digite o primeiro numero: "))
        b = float(input("Digite o segundo numero: "))

        if b != 0:
            resultado = a / b
            print("Resultado:", resultado)
        else:
            print("Nao pode dividir por zero.")

    elif opcao == 4:

        a = float(input("Digite o primeiro numero: "))
        b = float(input("Digite o segundo numero: "))

        resultado = a - b

        print("Resultado:", resultado)

    elif opcao == 5:

        a = float(input("Digite um numero: "))

        resultado = a * a

        print("Resultado:", resultado)

    elif opcao == 6:

        n = int(input("Digite n: "))

        resultado = 1

        for i in range(n):
            resultado = resultado * 2.72

        print("Resultado:", resultado)

    elif opcao == 7:

        x = float(input("Digite x: "))
        termos = int(input("Digite a quantidade de termos: "))

        resultado = 1
        termo = 1

        for i in range(1, termos):
            termo = termo * x / i
            resultado = resultado + termo

        print("Resultado aproximado:", resultado)

    elif opcao == 8:

        x = float(input("Digite x em radianos: "))
        termos = int(input("Digite a quantidade de termos: "))

        resultado = x
        termo = x
        sinal = -1

        for i in range(1, termos):

            termo = termo * x * x
            termo = termo / ((2 * i) * (2 * i + 1))

            resultado = resultado + sinal * termo

            sinal = sinal * -1

        print("Resultado aproximado:", resultado)

    elif opcao == 0:

        print("Programa encerrado.")
        break

    else:

        print("Opcao invalida.")