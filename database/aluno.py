import sqlite3
from random import randint
from database.banco import connect_db

class Aluno:
    """Modelo de dados da tabela alunos"""

    def __init__(self, al_id, nome, senha, data_nascimento, ano_matricula) -> None:
        self.al_id = al_id
        self.nome = nome
        self.senha = senha
        self.data_nascimento = data_nascimento
        self.ano_matricula = ano_matricula

    def __str__(self) -> str:
        return str(self.al_id) + ' ' + self.nome
    

def create(aluno: Aluno):
    """Insere um novo aluno no banco de dados"""
    connection, cursor = connect_db()

    try:
        al_id = generate_student_id(cursor, aluno)

        cursor.execute('INSERT INTO alunos (id, nome, senha, data_nascimento, ano_matricula) VALUES (?, ?, ?, ?, ?)',
                        (al_id, aluno.nome, aluno.senha, aluno.data_nascimento, aluno.ano_matricula))

    except sqlite3.IntegrityError:
        print('ID duplicado')
    
    connection.commit()
    connection.close()


def delete(al_id):
    """Deleta um aluno do banco de dados"""
    connection, cursor = connect_db()

    cursor.execute('DELETE FROM alunos WHERE id = ?', (str(al_id),))

    connection.commit()
    connection.close()


def list_students():
    connection, cursor = connect_db()

    cursor.execute('SELECT * FROM alunos')
    alunos_1 = cursor.fetchall() # Lista com os dados da tabela
    alunos_2: list[Aluno] = [] # Lista de Objetos(Aluno) com os dados da tabela

    for aluno in alunos_1:
        alunos_2.append(Aluno(aluno[0], aluno[1], aluno[2], aluno[3], aluno[4]))

    connection.close()

    return alunos_2

def generate_student_id(cursor: sqlite3.Cursor, aluno: Aluno):
    """Gera um id para o aluno"""
    cod = aluno.ano_matricula + '88901'

    for i in range(4):
        cod += str(randint(0, 9))

    return cod