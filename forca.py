import random

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

    if escolha == 5:
        break
    elif escolha == 1:
        
        forca(frutas)
    
    elif escolha == 2:
        forca(animal)
    elif escolha == 3:
        forca(personagens)
    else:
        print ("Código não reconhecido, tente novamente!")