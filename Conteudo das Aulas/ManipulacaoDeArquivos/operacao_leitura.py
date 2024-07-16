arquivo = open("lorem.txt", 'r')
#print(f'Texto Inteiro do Arquivo: \n{arquivo.read()}')


# len(linha) -> verifica o tamanho da linha se for zero ele para.
while len(linha := arquivo.readline()):
    print(linha)
arquivo.close()
