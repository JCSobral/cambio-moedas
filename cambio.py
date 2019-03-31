import requests
import json
import pandas as pd
import decimal
print("")
print("")
print("### CAMBIO DE MOEDAS EM TEMPO REAL ###")
print("")

url = "http://data.fixer.io/api/latest?access_key=4269a27be188915e860139581dbb8789"
print("Acessando base de dados...")

response = requests.get(url)
print(response)

if response .status_code == 200:
    
    print("Consegiu acessar base de dados!")
    print("Buscando informações das moedas...")
    
    dados = response.json()
    day = dados['date']
    
    euro_real = round(dados['rates']['BRL'] / dados['rates']['EUR'], 2)
    dollar_real = round(dados['rates']['BRL'] / dados['rates']['USD'], 2)
    bitcoin_real = round(dados['rates']['BRL'] / dados['rates']['BTC'], 2)
    
    print("")
    print("Dados do dia: %s/%s/%s" % (day[8:], day[5:7], day[0:4]))
    print("1 Euro =    R$ " "%.3f" % euro_real)
    print("1 Dollar =  R$ ""%.3f" % dollar_real)
    print("1 Bitcoin = R$ ""%.3f" % bitcoin_real)

    df = pd.DataFrame({'Moedas': ['Euro', 'Dollar', 'Bitcoin'], 'Valores (R$)': [euro_real, dollar_real, bitcoin_real]})
    df.to_csv("valores.csv", index=False, sep=";")

    print("Arquivo *.csv exportado com sucesso, para a pasta do projeto!")

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