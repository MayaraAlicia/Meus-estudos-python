import shutil
import random
import time
import string

VERDE='\033[92m'
RESET = '\033[0m'

tamanho = shutil.get_terminal_size()
largura = tamanho.columns

colunas = [0]*largura

print (VERDE + "--- APERTE CTRL+C PARA SAIR DA MATRIX ---" + RESET)
time.sleep(2)

try:
    while True:
        linha_atual = ''

        for i in range(largura):
            if colunas[i] == 0:
                if random.random() < 0.02:
                    colunas[i] = random.randint(5, 20)
            if colunas[i] > 0:
                caractere = random.choice(string.ascii_letters + string.digits)
                linha_atual += caractere
                colunas[i] -= 1

            else:
                linha_atual += " "
        
        print(VERDE + linha_atual + RESET)
        time.sleep(0.05)
         

except KeyboardInterrupt:
    print(RESET + "\n\n🔌 Desconectado da Matrix.")
