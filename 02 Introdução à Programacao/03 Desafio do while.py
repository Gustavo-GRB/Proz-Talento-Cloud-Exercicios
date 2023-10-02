# Desafio tentado simular do while  (não presente nativamente em Python)

i = 20
while True:
    if i == 13:
        i -= 1
        continue
    print(f"{i}º Andar")
    i -= 1

    if i == 0:
        break
