import os
import shutil
from pathlib import Path

# CRIA UMA ROTA PARA ACESSAR A PASTA ONDE SE DESEJA CRIAR OS ARQUIVOS DESEJADOS
ROOT_PATH = Path(__file__).parent

# CRIA UM NOVO DIRETORIO
#os.mkdir(ROOT_PATH / 'gerenciando_com_os_shutil')

arquivo = open(ROOT_PATH / "new.txt", 'w')
arquivo.close()
