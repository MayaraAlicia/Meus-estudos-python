import requests
import json
import time

def carregar_paises_validos():
    print ("Carregando lista de países...")
    url = "https://restcountries.com/v3.1/all?fields=name,independent"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            dados = response.json()
            paises_validos = set()
            for pais_info in dados:
                if pais_info.get('independent') == True:
                    nome_comum = pais_info['name']['common']
                    paises_validos.add(nome_comum.lower())


            print ("Pronto! A lista de países foi carregada com sucesso.")
            return paises_validos
        else:
            print (f"Erro ao carregar a lista de países. Código de status: {response.status_code}")
            return set() 
        
    except requests.exceptions.RequestException as e: 
        print (f"Ocorreu um erro de conexão ao carregar a lista de países: {e}")
        return None # Retorna None em caso de falha de conexão
    except Exception as e:
        print (f"Ocorreu um erro inesperado: {e}")
        return None

paises_validos = carregar_paises_validos()

if not paises_validos:
    print ("Não foi possível carregar o jogo. Sentimos muito :(")

else:
    total_paises = len(paises_validos)
    paises_acertados = set()
    pontos = 0

    print (f"----------------------------------------")
    time.sleep(0.5)
    print ("Bem-vindo ao jogos Atlas!")
    time.sleep(0.5)
    print ("O objetivo é muito simples: acertar o maior numero de países existentes")
    time.sleep(0.5)
    print ("A finalidade é testar quantoos países você conhece no mundo.")
    time.sleep(0.5)
    print (f"Existem ao todo {total_paises} países no mundo.")
    time.sleep(0.5)
    print ("É normal que não se conheça todos, então não se preocupe, o objetivo é se divertir!")
    time.sleep(0.5)
    print ("Para sair do jogo a qualquer momento, digite 'sair'.")
    time.sleep(0.5)
    print (f"----------------------------------------\n\n\n\n")
    time.sleep(0.5)

    while True:

        if pontos == total_paises:
            print ("Uau! Parabéns, você acertou todos os países do mundo!")
            break

        tentativa = input("\nDigite o nome de um país: ").strip().lower()
        if tentativa == 'sair':
            print ("Partida encerrada!\n\n")
            break
        if tentativa in paises_acertados:
            print (f"Você já acertou o país {tentativa.title()}! Tente outro.")
            continue
        elif tentativa in paises_validos:
            paises_acertados.add(tentativa)
            pontos += 1
            print (f"Parabéns! Você acertou o país {tentativa.title()}! Pontos: {pontos}")
        else:
            print (f"País {tentativa.title()} não reconhecido. Tente novamente.")

    time.sleep(0.5)
    print ("\n\n----------------------------------------")
    time.sleep(1)
    print (f"Você fez {pontos} pontos.")
    porcentagem = (pontos / total_paises) * 100
    print (f"Você acertou {porcentagem:.2f}% dos países existentes no mundo.")

    if porcentagem < 100:
        paises_faltantes = paises_validos - paises_acertados
        print ("Países que você não acertou:")
        for pais in sorted(paises_faltantes):
            time.sleep(0.1)  
            print (f"- {pais.title()}")

        print ("----------------------------------------")

    time.sleep(0.7)

    if porcentagem < 50:
        print ("O seu conhecimento geográfico é limitado, mas não desanime! Continue estudando e explorando o mundo.")
    
    elif 50 <= porcentagem < 80:
        print ("Bom trabalho! Você tem um conhecimento geográfico razoável, mas ainda há espaço para melhorias.")
    elif 80 <= porcentagem < 90:
        print ("Ótimo trabalho! Você tem um conhecimento geográfico sólido e está quase lá.")
    else:
        print ("Excelente! Você é um verdadeiro expert em geografia mundial!")