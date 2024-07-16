import sqlite3

conexao = sqlite3.connect("clientes.db")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row
# Maneira 1:
#try:
#    cursor.execute('INSERT INTO clientes (nome, email) VALUES (?, ?)', ('Teste 1', 'teste1@gmail.com'))
#    cursor.execute('INSERT INTO clientes (id, nome, email) VALUES (?, ?, ?)', (1, 'Teste 1', 'teste1@gmail.com'))
#except Exception as exc:
#    print(f'Ops! ocorreu um erro! {exc}')
#    conexao.rollback()
#finally:
#    conexao.commit()

# MANEIRA 2:
try:
    cursor.execute('INSERT INTO clientes (nome, email) VALUES (?, ?)', ('Teste 1', 'teste1@gmail.com'))
    cursor.execute('INSERT INTO clientes (id, nome, email) VALUES (?, ?, ?)', (1, 'Teste 1', 'teste1@gmail.com'))
    conexao.commit()
except Exception as exc:
    print(f'Ops! ocorreu um erro! {exc}')
    conexao.rollback()
