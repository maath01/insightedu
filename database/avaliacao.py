import sqlite3
from database.banco import connect_db
from database.connection_tables import materias_avaliacoes
from database.aluno import *
from random import randint
from datetime import datetime

class Avaliacao:

    def __init__(self, av_id=0, serie=0, bimestre=0, professor_id=0, turma_id=0, data_aplicacao=''):
        self.av_id = av_id
        self.serie = serie
        self.bimestre = bimestre
        self.professor_id = professor_id
        self.turma_id = turma_id
        self.data_aplicacao = data_aplicacao
    
    def __str__(self):
        return f'{self.av_id} - {self.serie} Serie, {self.bimestre} Bimestre, {self.data_aplicacao}'
    

def create(av: Avaliacao, materia: str):
    """Insere uma nova avaliação no banco de dados"""

    connection, cursor = connect_db()

    try:
        av_id = generate_av_id(av, materia, cursor)

        cursor.execute('INSERT INTO avaliacoes (id, serie, bimestre, professor_id, turma_id data_aplicacao) VALUES (?, ?, ?, ?)',
                       (av_id, av.serie, av.bimestre, av.professor_id, av.turma_id, av.data_aplicacao))
        connection.commit()
    
    except sqlite3.IntegrityError:
        print('ID duplicado')
    else:
        materias_avaliacoes(materia, av_id, cursor, connection)
        av.av_id = av_id
    
    connection.close()


def delete(av_id):
    """Deleta uma avaliação do banco de dados"""

    connection, cursor = connect_db()

    cursor.execute('DELETE FROM avaliacoes WHERE id = ?', (str(av_id),))
    cursor.execute(f'DELETE FROM materias_avaliacoes WHERE avaliacoes_id = ?', (str(av_id),))
    connection.commit()
    connection.close()


def list_evaluations():
    """Lista todas as avaliações do banco de dados"""

    connection, cursor = connect_db()

    cursor.execute('SELECT * FROM avaliacoes')
    avs_1 = cursor.fetchall() # Lista com os dados da tabela
    avs_2: list[Avaliacao] = [] # Lista de Objetos(Avaliação) com os dados da tabela

    for av in avs_1:
        avs_2.append(Avaliacao(av[0], av[1], av[2], av[3], av[4]))

    connection.close()

    return avs_2


def get(av_id):
    """Recupera uma avaliação do banco de dados"""
    connection, cursor = connect_db()

    cursor.execute('SELECT * FROM avaliacoes WHERE id = ?', (str(av_id),))
    row = cursor.fetchall()[0]
    avaliacao = Avaliacao(row[0], row[1], row[2], row[3], row[4], row[5])

    connection.close()

    return avaliacao

def generate_av_id(av: Avaliacao, materia, cursor):
    av_id = str(av.serie) + str(av.bimestre)

    cursor.execute('SELECT id FROM materias WHERE nome = ?', (materia,))
    id_materia = cursor.fetchall()[0][0]
    av_id += str(id_materia)

    for n in range(5):
        av_id += str(randint(0, 9))
    
    return av_id

def list_evaluations_by_teacher(teacher_id):
    """Lista as avaliações de um unico professor"""
    connection, cursor = connect_db()

    cursor.execute('SELECT * FROM avaliacoes WHERE professor_id = ?', (str(teacher_id),))
    avs_1 = cursor.fetchall() # Lista com os dados da tabela
    avs_2: list[Avaliacao] = [] # Lista de Objetos(Avaliação) com os dados da tabela

    for av in avs_1:
        avs_2.append(Avaliacao(av[0], av[1], av[2], av[3], av[4]))

    connection.close()

    return avs_2


def get_matter(av: Avaliacao):
    """Devolve a materia da avaliação"""
    connection, cursor = connect_db()

    cursor.execute('SELECT * FROM materias_avaliacoes WHERE avaliacoes_id = ?', (str(av.av_id),))
    materia_id = cursor.fetchall()[0][0]

    cursor.execute('SELECT * FROM materias WHERE id = ?', (str(materia_id),))
    materia = cursor.fetchall()[0][1]

    connection.close()

    return materia


def update_av(av_id,av: Avaliacao):
    """Atualiza um elemento no banco de dados"""
    connection, cursor = connect_db()

    data_atual = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 

    cursor.execute("UPDATE avaliacoes SET  serie= ?, bimestre = ?,professor_id  = ?,turma_id=?,data_aplicacao= ? WHERE id = ?",
                  ( av.serie, av.bimestre, av.professor_id, av.turma_id,data_atual, av_id))
    connection.commit()
    connection.close()  

