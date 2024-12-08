from banco import connect_db
import sqlite3
from random import randint


class Professor:
    """Modelo de dados da tabela professores"""

    def __init__(self, prof_id=0, nome='', email='', senha='', uf='', data_nascimento='') -> None:
        self.prof_id = prof_id
        self.nome = nome
        self.email = email
        self.senha = senha
        self.uf = uf
        self.data_nascimento = data_nascimento

    def __str__(self) -> str:
        return str(self.prof_id) + ' ' + self.nome
    
def create(professor: Professor):
    """Insere um novo professor no banco de dados"""
    connection, cursor = connect_db()

    try:
        prof_id = generate_teacher_id(cursor, professor)

        cursor.execute('INSERT INTO professores (id, nome, email, senha, uf, data_nascimento) VALUES (?, ?, ?, ?, ?, ?)',
                        (prof_id, professor.nome, professor.email, professor.senha, professor.uf, professor.data_nascimento))

    except sqlite3.IntegrityError:
        print('ID duplicado')
    
    connection.commit()
    connection.close()


def delete(prof_id):
    """Deleta um professor do banco de dados"""
    connection, cursor = connect_db()

    cursor.execute('DELETE FROM professores WHERE id = ?', (str(prof_id),))

    connection.commit()
    connection.close()


def list_teachers():
    connection, cursor = connect_db()

    cursor.execute('SELECT * FROM professores')
    profs_1 = cursor.fetchall() # Lista com os dados da tabela
    profs_2: list[Professor] = [] # Lista de Objetos(Professor) com os dados da tabela

    for prof in profs_1:
        profs_2.append(Professor(prof[0], prof[1], prof[2], prof[3], prof[4]))

    connection.close()

    return profs_2

def generate_teacher_id(cursor: sqlite3.Cursor, professor: Professor):
    """Gera um id para o professor"""
    escola = '88901'
    nascimento = professor.data_nascimento[6:]
    cod = nascimento + escola
    
    for n in range(3):
        cod += str(randint(0, 9))
    
    return cod

