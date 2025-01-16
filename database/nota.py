import sqlite3
from database.banco import connect_db
from database.connection_tables import materias_avaliacoes
from random import randint


class Nota:
    def __init__(self, nota_id=0, al_id=0, av_id=0, nota=0.0):
        self.nota_id = nota_id
        self.al_id = al_id
        self.av_id = av_id
        self.nota = nota

    def __str__(self):
        return f'{self.nota_id} - Aluno: {self.al_id}, Avaliação: {self.av_id}, Nota: {self.nota}'

def create(nota: Nota):
    """Insere uma nova nota no banco de dados."""

    connection, cursor = connect_db()

    try:

        nota_id = generate_nota_id(nota.al_id, nota.av_id)

        cursor.execute('INSERT INTO notas (id, aluno_id, avaliacao_id, nota) VALUES (?, ?, ?, ?)',
                       (nota_id, nota.al_id, nota.av_id, nota.nota))
        connection.commit()

    except sqlite3.IntegrityError:
        print('ID duplicado')

    connection.close()

def delete(nota_id):
    """Deleta uma nota do banco de dados."""

    connection, cursor = connect_db()

    cursor.execute('DELETE FROM notas WHERE id = ?', (nota_id,))
    connection.commit()
    connection.close()

def list_notes():
    """Lista todas as notas do banco de dados."""

    connection, cursor = connect_db()

    cursor.execute('SELECT * FROM notas')
    notas_1 = cursor.fetchall()  # Lista com os dados da tabela
    notas_2: list[Nota] = []  # Lista de objetos Nota com os dados da tabela

    for nota in notas_1:
        notas_2.append(Nota(nota[0], nota[1], nota[2], nota[3]))

    connection.close()

    return notas_2

def get(nota_id):
    """Recupera uma nota do banco de dados."""

    connection, cursor = connect_db()

    cursor.execute('SELECT * FROM notas WHERE id = ?', (nota_id,))
    row = cursor.fetchone()

    if row:
        nota = Nota(row[0], row[1], row[2], row[3])
    else:
        nota = None

    connection.close()

    return nota

def generate_nota_id(al_id, av_id):
    """Gera um ID único para a nota."""
    nota_id = f"{al_id}{str(av_id)[0:3]}"

    for _ in range(2):
        nota_id += str(randint(0, 9))
    
    return nota_id
