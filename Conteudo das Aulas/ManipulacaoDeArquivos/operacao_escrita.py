arquivo = open('testando.txt', 'w')

arquivo.write("Escrevendo dados em um novo arquivo.")
arquivo.writelines(["\nEscrevendo ", "novamente."])
arquivo.close()
