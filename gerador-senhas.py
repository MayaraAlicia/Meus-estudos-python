import random

simbolos = [
    '!', '@', '#', '$', '%', '&', '*', '(', ')', '-', '_', '=', '+',
    '[', ']', '{', '}', ';', ':', ',', '.', '<', '>', '/', '?',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' '
]


tamanho = int(input("Qual o tamanho desejado para a senha: "))
i = 0
senha_formando = []
while i < tamanho:
    random.shuffle(simbolos)
    caracter = simbolos[0]
    senha_formando.append(caracter)
    i = i+1
    
senha = ''.join(senha_formando)
print ("Senha: ",senha)
