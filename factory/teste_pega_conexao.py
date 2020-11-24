# -*- coding: utf-8 -*-
from factory.conexao_banco import Connection_factory

# escondeu os detalhes de criação do banco
# tratamento de erro omitido
connection=Connection_factory().get_connection()

cursor = connection.cursor()
cursor.execute('SELECT * from cursos')

for linha in cursor:
    print(linha)

connection.close()