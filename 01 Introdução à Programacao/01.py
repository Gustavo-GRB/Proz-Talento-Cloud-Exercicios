
quantidadeRodas = int(input("Entre com a quantidade de rodas: "))
kg = float(input("Entre com a quantidade em quilograma (KG): "))
quantidadePessoasVeiculo = int(
    input("Entre com a quantidade de pessoas no veículo: "))

if(quantidadeRodas == 2 and quantidadeRodas == 3):
    print("Categoria A")
elif(quantidadeRodas == 4 and quantidadePessoasVeiculo <= 8 and kg <= 3500):
    print("Categoria B")
elif(quantidadeRodas >= 4 and kg > 6000):
    print("Categoria E")
elif(quantidadeRodas >= 4 and quantidadePessoasVeiculo > 8):
    print("Categoria D")
elif(quantidadeRodas == 4 and (kg >= 3500 and kg <= 6000)):
    print("Categoria C")
else:
    print("Não foi possível identificar a categoria. Um ou mais Valores estão fora do padrão.")
