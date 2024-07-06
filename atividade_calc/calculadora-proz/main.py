def calculadora():

    while True:

        print("===== Calculadora Proz =====")
        print("A: Soma\n"
              "S: Subtração\n"
              "M: Multiplicação\n"
              "D: Divisão\n"
              "E: Sair")

        menu = input("Digite a opção desejada: ").upper()

        if menu == 'A':
            num1 = float(input(" Digite o primeiro valor: "))
            num2 = float(input(" Digite o segundo valor: "))
            resultado = num1 + num2
            print("Resultado: ", resultado)

        elif menu == 'S':
            num1 = float(input("Digite o primeiro valor: "))
            num2 = float(input("Digite o segundo valor: "))
            resultado = num1 - num2
            print("Resultado: ", resultado)

        elif menu == 'M':
            num1 = float(input("Digite o primeiro valor: "))
            num2 = float(input("Digite o segundo valor: "))
            resultado = num1 * num2
            print("Resultado: ", resultado)

        elif menu == 'D':
            num1 = float(input("Digite o primeiro valor: "))
            num2 = float(input("Digite o segundo valor: "))
            if num2 == 0:
                print("Erro: Divisão por zero não permitida")
            else:
                resultado = num1 / num2
                print("----------------------")
                print("Resultado: ", resultado)
                print("----------------------")

        elif menu == 'E':
            print("Saindo..")
            break

        else:
            print("Essa opção não existe...")


calculadora()
