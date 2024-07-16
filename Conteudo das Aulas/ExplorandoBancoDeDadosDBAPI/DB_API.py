import sqlite3

conexao = sqlite3.connect("clientes.db")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row


def criar_tabela(cursor):
    cursor.execute(
        "CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT,"
        " nome VARCHAR(100), email VARCHAR(150))")
    conexao.commit()


def inserir_registro(conexao, cursor, nome, email):
    data = (nome, email)
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?);", data)
    conexao.commit()


def atualizar_registro(conexao, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute("UPDATE clientes SET nome = ?, email = ? WHERE id=?;", data)
    conexao.commit()


def excluir_registro(conexao, cursor, id):
    data = (id,)  #colocar virgula quando passar tupla com um único valor
    cursor.execute("DELETE FROM clientes WHERE id=?;", data)
    conexao.commit()

def inserir_muitos(conexao, cursor, dados):
    cursor.executemany("INSERT INTO clientes (nome, email) VALUES (?, ?)", dados)
    conexao.commit()

def recuperar_cliente(cursor, id):
    cursor.execute("SELECT * FROM clientes WHERE id=?;", (id,))
    return cursor.fetchone()


def listar_clientes(cursor):
    return cursor.execute("SELECT * FROM clientes;")


clientes = listar_clientes(cursor)
for cliente in clientes:
    print(dict(cliente))

cliente = recuperar_cliente(cursor, 1)
print(dict(cliente))
#print(cliente['id'])

#EXEMPLO DE USO COM DADOS VOLTANDO EM DICT:
print(f'Seja bem vind@ ao sistema {cliente["nome"]}')


#dados = [
    #('Beto', 'bet89@outlook.com'),
    #('Carlos', 'carlao@outlook.com'),
    #('Daiane', 'dai_ne@gmail.com'),
#]

atualizar_registro(conexao, cursor, 'Ana Andrade', 'aninha@gmail.com', 1)
excluir_registro(conexao, cursor, 2)
#inserir_muitos(conexao, cursor, dados)
