def calculadora(fator1, fator2, operador):
    if(operador == "+"):
        return fator1 + fator2
    elif(operador == "-"):
        return fator1 - fator2
    elif(operador == "*"):
        return fator1 * fator2
    elif(operador == "/"):
        try:
            resultado = fator1 / fator2
            return resultado
        except ZeroDivisionError:
            print("Impossível dividir por 0!")
    else:
        return 0


print("Calculadora")
fator1 = float(input("Digite o primeiro número: "))
operador = str(input("\nDigite o operador\n(+) ou (-) ou (/) ou (*): "))
fator2 = float(input("\nDigite o segundo número: "))

print("Resultado da operação: ", calculadora(fator1, fator2, operador))
