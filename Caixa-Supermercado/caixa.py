produtos = [
    {'codigo': 1, 'nome': 'Bolo', 'preco': 20.50},
    {'codigo': 2, 'nome': 'Bolacha', 'preco': 10.00},
    {'codigo': 3, 'nome': 'Pudim','preco': 15.00},
    {'codigo': 4, 'nome': 'Brigadeiro', 'preco': 5.50},
    {'codigo': 5, 'nome': 'Torta', 'preco': 25.00}
    ]

total = 0
compras= []

oq = int(input("Insira o codigo do produto ou 0 para sair: "))

while oq != 0:
    if oq == 1:
        total = total + produtos[0]['preco']
        print (f"Total: R${total:.2f}")
        compras.append(produtos[0]['nome'])
        
    elif oq == 2:
        total = total + produtos[1]['preco']
        print (f"Total: R${total:.2f}")
        compras.append(produtos[1]['nome'])

    elif oq == 3:
        total = total + produtos[2]['preco']
        print (f"Total: R${total:.2f}")
        compras.append(produtos[2]['nome'])

    elif oq == 4:
        total = total + produtos[3]['preco']
        print (f"Total: R${total:.2f}")
        compras.append(produtos[3]['nome'])

    elif oq == 5:
        total = total + produtos[4]['preco']
        print (f"Total: R${total:.2f}")
        compras.append(produtos[4]['nome'])

    else:
        print("Código invalido!")
    oq = int(input("Insira o codigo do produto ou 0 para sair: "))

print (f"\nTotal da compra: {total}")
compras.sort()
print (f"Itens comprados: {compras}")
