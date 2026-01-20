import random
import time

while True:
    choice = int(input("Escolha o jogo que deseja jogar!\n\n1. Jogo da forca\n2. Quente ou Frio Numérico\n3. Desafio da Sorte\n4. ♣21♠\n5. Sair\n"))
    
    if choice == 1:
            
        def forca (lista):
            palavra_sorteada = random.choice(lista).upper()
            letras = list(palavra_sorteada)
            palavra_oculta = []
            for letra in palavra_sorteada:
                if letra == ' ':
                    palavra_oculta.append('   ')
                else:
                    palavra_oculta.append('_ ')
                
                
            chutes = 0
                
            letras_chutadas = []
                
            tentativa = ""
                
            while chutes < 6:
                    
                posicoes_encontradas = []
                print ("\nPalavra: "," ".join(palavra_oculta))
                tentativa = input("Digite uma letra: ").upper()
                    
                if len(tentativa) != 1:
                    print ("NÃO TENTE ROUBAR DIGITANDO MAIS DE UMA LETRA >:(\nVocê perdeu 2 vidas por isso :(\n")
                    chutes += 2
                    continue
                        
                if tentativa in letras_chutadas:
                    print ("Você já tentou essa letra!")
                    continue
                else:
                    letras_chutadas.append(tentativa)
                        
                    if tentativa in letras:
                        for i in range(len(letras)):
                            if tentativa == ' ':
                                palavra_oculta[i] = ' '
                            elif letras[i] == tentativa:
                                palavra_oculta[i] = tentativa
                        print (f"'{tentativa}' esta na palavra!")
                    else:
                        chutes += 1
                            
                print(f"Vidas restantes: {6 - chutes}\n")
                print (f"Letras tentadas: "," ".join(letras_chutadas))
            
                if all(letra != "_ " for letra in palavra_oculta if letra.strip() !=  0):
                    print (f"Parabéns! A palavra era: {palavra_sorteada}\n\n\n")
                    break
                    
            if chutes >= 6:
                print(f"Game over! A palavra era: {palavra_sorteada}\n\n\n")
                
                
        personagens= ["Vanellope", "Malevola", "Naveen", "Mushu", "Baymax", "Elsa", "Linguini", "Buzz Lightyear", "Edna Moda", "Nemo", "Boo"]
        frutas= ["Jabuticaba", "Kiwi", "Manga", "Abacate", "Abacaxi", "Atemoia", "Pitanga", "Tomate", "Acerola"]
        animal = ["Baleia", "Ornintorrinco", "Tamandua", "Capivara", "Quati", "Suricata"]

        print ("*** Jogo da Forca ***")
        print ("\nRegras: \n- Adivinhe a palavra letra por letra.\n- Você tem 6 vidas. Use-as com sabedoria!\n- Letras repetidas não consomem vidas.\n")

        while True:
            escolha = int(input("1. Frutas\n2. Animal\n3. Personagens da Disney\n4. Sair\nEscolha um tema: "))

            if escolha == 4:
                break
            elif escolha == 1:
                
                forca(frutas)
            
            elif escolha == 2:
                forca(animal)
            elif escolha == 3:
                forca(personagens)
            else:
                print ("Código não reconhecido, tente novamente!")
            
    elif choice == 2:
        while True:
            print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nVamos jogar um jogo, você precisa acertar o numero!\nDica: ele esta entre 1 e 100")
            chute = int(input("Digite um numero: "))
            numero = random.randint(1,100)
            chutes = 0
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
            if chutes < 5:
                print ("Você foi incrivel!")
            elif chutes <= 10:
                print ("Você foi bem!")
            elif chutes <= 15:
                print ("Você foi mediano!")
            else:
                print ("Você foi muito ruim mds!")
            
            resposta = int(input("Digite 1 para sair, ou 2 para jogar novamente!\n"))
            if resposta == 1:
                break
            
    elif choice == 3:
        while True:
            jogadores = []
            
            qnts = int(input("Quantidade de competidores: "))
            i = 0
            while i < qnts:
                
                nome = input(f"Qual o nome do {i+1}° jogador: ")
                numeros = []
                contador = 0
                while contador < 9:
                    num = int(input(f"Digite o {contador +1}° numero: "))
                    numeros.append(num)
                    contador += 1
                jogador = {'nome': nome,  'numeros': numeros, 'acertos': 0}
                jogadores.append(jogador)
                i += 1
            i = 0
            numeros_aleatorios= random.sample(range(1,100), 10)
            
            for jogador in jogadores:
                for numero in jogador['numeros']:
                    if numero in numeros_aleatorios:
                        jogador['acertos'] +=1
            
            maior_acerto = 0
            
            for jogador in jogadores:
                if jogador['acertos'] > maior_acerto:
                    maior_acerto = jogador['acertos']
            
            ganhadores = []
            for jogador in jogadores:
                if jogador['acertos'] == maior_acerto:
                    ganhadores.append(jogador['nome'])
                    ganhador = jogador['nome']
            
            indice = 0
            
            while indice < len(numeros_aleatorios):
                print ("\n\n\nSorteando...")
                time.sleep(1.5)
                print (f"{indice+1}° numero sorteado: {numeros_aleatorios[indice]}.")
                for jogador in jogadores:
                    if numeros_aleatorios[indice] in jogador['numeros']:
                        print (f"{jogador['nome']} acertou esse numero!")
                        
                indice += 1
            print (f"\n\n\nOs numeros sorteados foram: {', '.join(sorted(map(str, numeros_aleatorios)))}!")
            if len(ganhadores) == 1:
                print (f"O ganhador foi {ganhador}! Parabéns!")
            
            else:
                print (f"Houve um empate entre os jogadores: {', '.join(ganhadores)}! Parabéns a eles!")
                
            print (f"#Pontuação#")
            for jogador in jogadores:
                print (f"{jogador['nome']}: {jogador['acertos']} ponto(s)")
            variando = int (input("1. Jogar novamente\n2. Sair\nDigite o que quer fazer: \n\n\n\n\n"))
            if variando == 2:
                break
            else:
                continue
        
            
    elif choice == 5:
        break
    

    elif choice == 4:
        jogar_novamente = "S"
        pontos_do_usuario = 0
        pontos_da_maquina = 0
        while jogar_novamente == "S":
        
        
            print("\n" + "=" * 40)
            print("Bem-vindo ao Jogo 21 (Blackjack)!".center(40))
            print("=" * 40)
            print(
                """
                *** REGRAS ***
                1. O objetivo é chegar o mais perto possível de 21 pontos.
                2. Cartas numéricas valem seu valor (2 a 10).
                3. Valete (J), Dama (Q) e Rei (K) valem 10.
                4. O Ás (A) valem 1
                5. Você começa com 2 cartas e pode:
                   - COMPRAR: pedir mais uma carta.
                   - PARAR: manter sua pontuação atual.
                6. Se ultrapassar 21 pontos, perde automaticamente!
                """
            )
            print("=" * 40 + "\n")
            start = input("Digite (J) para começar a jogar:  ").upper()
            if start == "J":
                
                
                ##é aqui q o codigo realmente começa
                while True:
                    espadas = ["♠ A", "♠ 2","♠ 3","♠ 4","♠ 5","♠ 6","♠ 7","♠ 8","♠ 9","♠ J","♠ Q","♠ K"]
                    paus = ["♣ A", "♣ 2","♣ 3","♣ 4","♣ 5","♣ 6","♣ 7","♣ 8","♣ 9","♣ J","♣ Q","♣ K"]
                    copas = ["♥ A", "♥ 2","♥ 3","♥ 4","♥ 5","♥ 6","♥ 7","♥ 8","♥ 9","♥ J","♥ Q","♥ K"]
                    ouros = ["♦ A", "♦ 2","♦ 3","♦ 4","♦ 5","♦ 6","♦ 7","♦ 8","♦ 9","♦ J","♦ Q","♦ K"]
                    
                    baralho = espadas + paus + copas + ouros
                    random.shuffle(baralho)
                    ##é criado uma lista para cada naipe e então é juntado tudo em um unico baralho
                    ##e usado um random para embaralhar tudo
                    
                    
                    naipes_usuario = []
                    valores_usuario =[]
                    naipes_maquina = []
                    valores_maquina = []
                    
                    carta = baralho.pop(0)
                    naipe, valor = carta.split()
                    naipes_usuario.append(naipe)
                    valores_usuario.append(valor)
                
                    carta = baralho.pop(0)
                    naipe, valor = carta.split()
                    naipes_usuario.append(naipe)
                    valores_usuario.append(valor)
                
                    carta = baralho.pop(0)
                    naipe, valor = carta.split()
                    naipes_maquina.append(naipe)
                    valores_maquina.append(valor)
                    carta = baralho.pop(0)
                    naipe, valor = carta.split()
                    naipes_maquina.append(naipe)
                    valores_maquina.append(valor)
                    
                    ##cada competidor (usuario e maquina) tem 2 listas, 1 com os naipes das cartas q pegou e outro com o valor
                    ##entao o sistema escolhe a 1ª carta do baralho embaralhado e separa o naipe e o valor armazenando nas suas respectivas listas
            
                    print ("Embaralhando.")
                    time.sleep(0.5)
                    print ("Embaralhando..")
                    time.sleep(0.5)
                    print ("Embaralhando...")
                    time.sleep(0.5)
            
                    ##Então as cartas sorteadas para ele e 1 das 2 sorteadas para a maquina são mostrados:
                    print("\n=== SUAS CARTAS ===")
                    print ("")
                    print ("┌──────┐   ┌──────┐")
                    print(f"| {naipes_usuario[0]}    |   | {naipes_usuario[1]}    |")
                    print(f"|      |   |      |")
                    print(f"|   {valores_usuario[0]}  |   |   {valores_usuario[1]}  |")
                    print(f"|      |   |      |")
                    print(f"└──────┘   └──────┘")
                    time.sleep(1.5)
                    
            
                    print("\n\n=== CARTAS DA CASA ===\n")
                    print ("")
                    time.sleep(1)
                    print ("┌──────┐   ┌──────┐")
                    print(f"| {naipes_maquina[0]}    |   |      |")
                    print(f"|      |   |      |")
                    print(f"|   {valores_maquina[0]}  |   | ???? |")
                    print(f"|      |   |      |")
                    print(f"└──────┘   └──────┘")
                    print("")
                    time.sleep(0.5)
                    
                    
                    ##aqui é calculado a pontuação do usuario e da maquina
                    ##tem tanto if elif pq existe a opção de valores "A", "J" e etc q n são numeros
                    pontos_usuario = 0
                    if valores_usuario[0] == 'A':
                        pontos_usuario = pontos_usuario + 1
                    elif valores_usuario[0] in ['J', 'K' , 'Q']:
                        pontos_usuario = pontos_usuario + 10
                    else:
                        pontos_usuario = int(valores_usuario[0])
                        
                    if valores_usuario[1] == 'A':
                        pontos_usuario = pontos_usuario + 1
                    elif valores_usuario[1] in ['J' , 'K' , 'Q']:
                        pontos_usuario = pontos_usuario + 10
                    else:
                        pontos_usuario = pontos_usuario+int(valores_usuario[1])
                        
                        
                    pontos_casa = 0
                    if valores_maquina[0] == 'A':
                        pontos_casa = pontos_casa + 1
                    elif valores_maquina[0] in ['J', 'K' , 'Q']:
                        pontos_casa = pontos_casa + 10
                    else:
                        pontos_casa = int(valores_maquina[0])
                        
                    if valores_maquina[1] == 'A':
                        pontos_casa = pontos_casa + 1
                    elif valores_maquina[1] in ['J' , 'K' , 'Q']:
                        pontos_casa = pontos_casa + 10
                    else:
                        pontos_casa = pontos_casa+int(valores_maquina[1])
                        
                    ##A variavel "deseja" é a escolha do usuario de comprar ou manter, para iniciar o while ela começa sem valor nenhum
            
                    deseja = ""
                    
                    ##o i aqui é o indice q vai começar a mostrar, como ja mostrou antes o 0 e 1 aqui começa com 2
                    i = 2
                    
                    ##o while continua se o usuario não clicar em P ou se os pontos do usuario n ultrapassaram 21
                    while deseja != "P" and pontos_usuario <= 21:
                        
                        ##aqui o usuario escolhe manter ou não
                        deseja = input("\nDeseja COMPRAR (C) ou PARAR (P)?  ").upper()
                        
                        ##se ele escolheu comprar o if é acionado, nele é adicionado 1 carta para o jogador e mostrado a ele
                        if deseja == "C":
                            carta = baralho.pop(0)
                            naipe, valor = carta.split()
                            naipes_usuario.append(naipe)
                            valores_usuario.append(valor)
                            
                            time.sleep(0.5)
                            print (f"Você comprou:\n┌──────┐\n| {naipes_usuario[i]}    |\n|      |\n|   {valores_usuario[i]}  |\n|      |\n└──────┘")
                            
                            ##esse if ainda dentro da escolha comprar do jogador é para adicionar a pontuação do usuario a carta comprada
                            if valor == 'A':
                                pontos_usuario = pontos_usuario + 1
                            elif valor in ['J' , 'K' , 'Q']:
                                pontos_usuario = pontos_usuario + 10
                            else:
                                pontos_usuario = pontos_usuario+int(valor)
                                
                        ##esse else é caso o jogador escolha parar e não comprar mais
                        else:
                            
                            print ("\nVocê parou.\nÉ a vez da casa!")
                            print (f"Cartas da casa: ")
                            print ("┌──────┐   ┌──────┐")
                            print(f"| {naipes_maquina[0]}    |   | {naipes_maquina[1]}    |")
                            print(f"|      |   |      |")
                            print(f"|   {valores_maquina[0]}  |   |   {valores_maquina[1]}  |")
                            print(f"|      |   |      |")
                            print(f"└──────┘   └──────┘")
                            print("")
                            
                            time.sleep(0.8)
                            print ("Casa esta decidindo se quer comprar.")
                            time.sleep(0.8)
                            print ("Casa esta decidindo se quer comprar..")
                            time.sleep(0.8)
                            print ("Casa esta decidindo se quer comprar...")
                            print ("")
                            i = 2
                            
                            if pontos_casa >= 16:
                                time.sleep(1)
                                print ("A casa escolheu não comprar.")
                            
                            else:
                                while pontos_casa <= 16:
                                    time.sleep(1)
                                    
                                    print ("Casa escolheu comprar!")
                                    time.sleep(1)
                                    carta = baralho.pop(0)
                                    naipe, valor = carta.split()
                                    naipes_maquina.append(naipe)
                                    valores_maquina.append(valor)
                                    print (f"Casa comprou: \n┌──────┐\n| {naipes_maquina[i]}    |\n|      |\n|   {valores_maquina[i]}  |\n|      |\n└──────┘")
                                    if valores_maquina[i] == 'A':
                                        pontos_casa = pontos_casa + 1
                                    elif valores_maquina[i] in ['J' , 'K' , 'Q']:
                                            pontos_casa = pontos_casa + 10
                                    else:
                                            pontos_casa = pontos_casa+int(valores_maquina[i])
                                    i = i+1
                            print("\n\n\n")
                            time.sleep(2)
                            print ("Pontuação final:")
                            print ("Casa: ", pontos_casa)
                            print ("Usuario: ", pontos_usuario)
                            
                            time.sleep(0.3)
                            if pontos_casa > 21:
                                print("\n╔═════════════════════════════════╗")
                                print("║  A CASA ESTOUROU! VOCÊ VENCEU! ║")
                                print("╚═════════════════════════════════╝")
                                pontos_do_usuario = pontos_do_usuario + 1
                            elif pontos_usuario > pontos_casa:
                                print("\n╔════════════════════════╗")
                                print("║ PARABÉNS! VOCÊ VENCEU! ║")
                                print("╚════════════════════════╝")
                                pontos_do_usuario = pontos_do_usuario + 1
                            elif pontos_casa > pontos_usuario:
                                print("\n╔═══════════════════════════╗")
                                print("║ QUE PENA! A CASA VENCEU! ║")
                                print("╚═══════════════════════════╝")
                                pontos_da_maquina = pontos_da_maquina + 1
                            else: # pontos_usuario == pontos_casa
                                print("\n╔═════════════════════╗")
                                print("║      É UM EMPATE!     ║")
                                print("╚═════════════════════╝")
                                pontos_do_usuario = pontos_do_usuario + 1
                                pontos_da_maquina = pontos_da_maquina + 1
                        i = i +1
                    if pontos_usuario > 21:
                        
                        print("\n╔════════════════════════╗")
                        print("║    VOCÊ ESTOUROU!     ║")
                        print("╚════════════════════════╝")
                        pontos_da_maquina = pontos_da_maquina +1
                        
                    
                    print ("Pontuação: ")
                    print ("Usuario: ", pontos_do_usuario)
                    print ("Maquina: ", pontos_da_maquina)
                    jogar_novamente = input("\nDeseja jogar novamente? (S/N): ").upper()
                    if jogar_novamente != "S":
                        if pontos_da_maquina > pontos_do_usuario:
                            print ("Que pena você perdeu :(")
                        elif pontos_do_usuario > pontos_da_maquina:
                            print ("PARABÉNS! Você venceu a casa!")
                        else:
                            print ("Parece que temos um empate!")
                        print("\nObrigado por jogar! Até a próxima!\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                        break
                    print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    else:
        print ("Código invalido")
