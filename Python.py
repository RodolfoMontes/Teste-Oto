import csv
import unicodedata
import re

## Referencia https://www.otaviomiranda.com.br/2020/normalizacao-unicode-em-python/
## https://docs.python.org/3/library/csv.html
def remove_acentos(string: str) -> str:
    normalize = unicodedata.normalize('NFD', string)
    return normalize.encode('ascii','ignore').decode('utf-8').upper()


with open('natal2021.csv', 'r',encoding='utf-8') as arquivo:
 ## Transformando os dados em um dicionário. (Ele é um gerador, eficiente para o uso de memória);
    dados = [x for x in csv.DictReader(arquivo)]

## Criando o segundo arquivo com as informações toda tratada.
with open('natal2021_tratado.csv', 'w',encoding='utf-8') as arquivo:
    populando_arquivo = csv.writer(
        arquivo,
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_ALL
    )

    titulo = dados[0].keys()
    titulo = list(titulo)
    populando_arquivo.writerow(

        [
            titulo[1],
            titulo[2],
            'CITY_ASCII'
        ]
    )
    ## Populando o arquivo.
    for dado in dados:
        dado['CITY_ASCII'] = remove_acentos((dado['CITY'].strip()))

        phone_tratado = re.findall('[0-9]', dado['PHONE'].strip())
        phone_tratado = ''.join(phone_tratado)
        populando_arquivo.writerow(
            [
                dado['CITY'].strip(),
                phone_tratado,
                dado['CITY_ASCII']
            ]
        )