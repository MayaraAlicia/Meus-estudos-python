import requests
import json

print ("Fazendo pedido para a API...")
print ("Digite 0 para sair a qualquer momento.")

while True:

    escolha_pokemon = input("\nDigite o nome em inglês de um Pokémon para buscar (ex: bulbasaur, charmander, squirtle): ").strip().lower()
    url = f"https://pokeapi.co/api/v2/pokemon/{escolha_pokemon}"
    response = requests.get(url)

    if escolha_pokemon == "0":
        print("Saindo do programa. Até mais!")
        break

    if response.status_code == 200:
        print("Pedido bem-sucedido!\n")
        dados_pokemon = response.json()
        print(f"Nome do Pokémon: {dados_pokemon['name']}")
        print(f"ID do Pokémon: {dados_pokemon['id']}")
        print (f"Peso do Pokémon: {dados_pokemon['weight']}")

        print ("Habilidades:")
        for habilidade in dados_pokemon['abilities']:
            print(f"- {habilidade['ability']['name']}")

        url_imagem = dados_pokemon['sprites']['front_default']
        print(f"URL da imagem do Pokémon: {url_imagem}")
        print ("------------------------------------------")

    else:
        print (f"Opa, algo deu errado! Código de status: {response.status_code} ")