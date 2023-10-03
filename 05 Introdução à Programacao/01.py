import datetime

continuar = True
while (continuar):
    try:
        anoAtual = datetime.datetime.now().year
        nome = str(input("Digite o seu nome completo: "))
        nascimento = int(
            input(f"Ano de nascimento entre 1922 e {anoAtual-1}: "))

        if (nascimento < 1922 or nascimento >= anoAtual):
            print("Ano inválido!")
            continue

        idade = anoAtual - nascimento
        continuar = False
        print(f"{nome} em {anoAtual} completou, ou completará {idade} "
              "de idade")
    except Exception as err:
        print("Valor inválido")
        print(err)
        continuar = True
