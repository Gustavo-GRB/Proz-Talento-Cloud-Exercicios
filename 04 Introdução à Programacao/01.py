def calculadora(fator1, fator2, operador):
    if(operador == 1):
        return fator1 + fator2
    elif(operador == 2):
        return fator1 - fator2
    elif(operador == 3):
        return fator1 * fator2
    elif(operador == 4):
        try:
            resultado = fator1 / fator2
            return resultado
        except ZeroDivisionError:
            print("Impossível dividir por 0!")


continuar = True
while(continuar):
    print("\nDigite o número da operação deseja fazer: ")
    operador = (int(input("1: Soma \n2: Subtração \n3: Multiplicação "
                          "\n4: Divisão \n0: Sair \n")))

    if(operador <= -1 or operador >= 5):
        print("Essa opção não existe")
        continue
    elif(operador) == 0:
        print("Saindo...")
        continuar = False
        break

    fator1 = float(input("\nDigite o primeiro número: "))
    fator2 = float(input("Digite o segundo número: "))

    print("-> Resultado da operação: ", calculadora(fator1, fator2, operador))
