lista_produtos = ['máscaras faciais', 'batons', 'esmaltes',
                  'perfumes', 'loções', 'xampus', 'sabonetes', 'delineadores']

lista_produtos[1] = 'rímel'
lista_produtos[4] = 'cremes hidratantes'

lista_produtos.pop()

# desafio adicional
lista_produtos.append('Pó compacto')
lista_produtos.append('Blush')

for elemento in lista_produtos:
    print(elemento)
