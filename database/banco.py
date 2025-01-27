"""
Modulo que contem funções relacionadas ao banco de dados
"""

import sqlite3
import os.path

def connect_db():
    """Cria a conexão com o banco de dados e o cursor"""
    connection = sqlite3.connect('database/banco.db')
    cursor = connection.cursor()
    return connection, cursor

def create_database():
    """Cria o banco de dados se ele ainda não existir"""

    if not os.path.exists('database/banco.db'):
        connection, cursor = connect_db()

        # Cria todas as tabelas do banco
        with open('database/schema.sql') as file:
            commands = file.read().split(';')
        
        for command in commands:
            # print(command)
            cursor.execute(command)
            connection.commit()

        # Adiciona dados as tabelas
        with open('database/insert.sql') as file:
            commands = file.read().split(';')
        
        for command in commands:
            # print(command)
            cursor.execute(command)
            connection.commit()

        connection.close()

def check_login(categoria, user_id, nome, senha):
    tabela = ''
    if categoria == 'aluno':
        tabela = 'alunos'
    elif categoria == 'professor':
        tabela = 'professores'
    elif categoria == 'coordenador':
        tabela = 'coordenadores'
    elif categoria == 'gestor':
        tabela = 'gestores'

    connection, cursor = connect_db()
    user = None

    try:
        cursor.execute(f"SELECT * FROM {tabela} WHERE id = ? AND nome = ? AND senha = ?", (user_id, nome, senha))
        user = cursor.fetchone()
    except:
        pass

    return user

def search(table, column, attribute):
    """Pesquisa por um atributo especifico em uma tabela"""
    connection, cursor = connect_db()

    try:
        cursor.execute(f'SELECT * FROM {table} WHERE {column} = ?', (str(attribute),))
        row = cursor.fetchall()[0]
    except:
        row = None
    
    return row

