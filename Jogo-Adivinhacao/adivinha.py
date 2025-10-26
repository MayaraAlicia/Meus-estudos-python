import random


while True:
    print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nVamos jogar um jogo, você precisa acertar o numero!\nDica: ele esta entre 1 e 100")
    chute = int(input("Digite um numero: "))
    numero = random.randint(1,100)
    chutes = 1
    while chute != numero:
        if chute < numero:
            print (f"\nO numero que você quer achar é maior que {chute}")
            chutes = chutes + 1
        else:
            print (f"\nO numero que você quer achar é menor que {chute}")
            chutes = chutes + 1
        chute = int(input("Digite um numero: "))
    print (f"\nParabens! Você acertou, o numero era {numero}.")
    print (f"Você chutou {chutes} vezes!")
    if chutes == 1:
        print ("Sensacional! Você acertou de primeira!")
    if chutes < 5:
        print ("Você foi incrivel!")
    elif chutes <= 10:
        print ("Você foi bem!")
    elif chutes <= 15:
        print ("Você foi mediano!")
    else:
        print ("Você foi muito ruim mds!")
    
    resposta = int(input("Digite qualquer numero ou 1 se não deseja jogar de novo\n"))
    if resposta == 1:
        break
