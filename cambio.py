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