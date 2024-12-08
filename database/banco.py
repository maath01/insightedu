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
            print(command)
            cursor.execute(command)
            connection.commit()

        # Adiciona dados as tabelas
        with open('database/insert.sql') as file:
            commands = file.read().split(';')
        
        for command in commands:
            print(command)
            cursor.execute(command)
            connection.commit()

        connection.close()
create_database()
connect_db()