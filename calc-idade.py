nome = input("Digite seu nome completo: ")
while True:
    try:
        ano_nascimento = int(input("Digite seu ano de nascimento (entre 1922 e 2021): "))
        if 1922 <= ano_nascimento <= 2021:
            break
        else:
            print("Ano de nascimento inválido. Digite um ano entre 1922 e 2021.")
    except ValueError:
        print("Entrada inválida. Digite um ano válido.")

idade = 2022 - ano_nascimento
print(f"{nome}, você completou ou completará {idade} anos em 2022.")