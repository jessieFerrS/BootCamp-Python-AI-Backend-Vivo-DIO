from pathlib import Path

try:
    arquivo = open("meu-arquivo.py")
except FileNotFoundError:
    print("Arquivo não encontrado!")

ROOT_PATH = Path(__file__).parent

try:
    arquivo = open(ROOT_PATH / "gerenciando_com_os_shutil")
except IsADirectoryError as exc:
    print(f'Não foi possível abrir o arquivo: {exc}')
