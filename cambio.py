import requests
import json

url = "http://data.fixer.io/api/latest?access_key=4269a27be188915e860139581dbb8789"
print("Acessando base de dados...")
response = requests.get(url)
print(response)
if response .status_code == 200:
    print("Consegiu acessar base de dados!")
    print("Buscando informações das moedas...")
    dados = response.json()
    euro_real = dados['rates']['BRL'] / dados['rates']['EUR']
    dollar_real = dados['rates']['BRL'] / dados['rates']['USD']
    bitcoin_real = dados['rates']['BRL'] / dados['rates']['BTC']
    print("1 Euro = R$ " "%.2f" % euro_real)
    print("1 Dollar = R$ ""%.2f" % dollar_real)
    print("1 Bitcoin = R$ ""%.2f" % bitcoin_real)
else:
    print("Site com problemas!")



# ATUALIZANDO A APLICAÇÃO DO PYTHON, NO GITHUB, APÓS ALTERAÇÕES:

  # Realizar alterações, normalmente, no código

  # Entrar no Git (botão direito sobre a pasta e selecionar Git Bash)

  # Digitar "git status"

  # Verificar se os arquivos alterados aparecem em vermelho (ok, foram alterados)

  # Digitar "git add .", para salvar alterações no computador

  # Digitar "git status"

  # Verificar se os arquivos alterados aparecem em verde (ok, foram carregados no git)

  # Digitar " git commit -m 'Inserir entre aspas o texto a respeito das alterações feitas"

  # Digitar "git push origin master", para enviar para o site do GitHub

  # Encontrar o histórico de alterações no Git Hub