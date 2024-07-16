import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent
COLUNA_ID = 0
COLUNA_NOME = 1


try:
    with open(ROOT_PATH / 'usuarios.csv', 'w', newline='', encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(['id', 'nome'])
        escritor.writerow(['1', 'Ana'])
        escritor.writerow(['2', 'Beto'])
except IOError as exc:
    print(f'Erro ao criar o arquivo. {exc}')

#try:
#    with open(ROOT_PATH / 'usuarios.csv', 'r', encoding="utf-8") as arquivo:
#        leitor = csv.reader(arquivo)
#        for row in leitor:
#            print(row)
#except IOError as exc:
#    print(f'Erro ao criar o arquivo. {exc}')

try:
    with open(ROOT_PATH / 'usuarios.csv', 'r', newline='',encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        for idx, row in enumerate(leitor):
            if idx == 0:
                continue
            print(f'ID:{row[COLUNA_ID]}')
            print(f'NOME:{row[COLUNA_NOME]}')
except IOError as exc:
    print(f'Erro ao criar o arquivo. {exc}')
