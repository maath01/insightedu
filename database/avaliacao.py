import sqlite3
from database.banco import connect_db
from database.connection_tables import materias_avaliacoes
from random import randint

class Avaliacao:

    def __init__(self, av_id=0, serie=0, bimestre=0, data_aplicacao=''):
        self.av_id = av_id
        self.serie = serie
        self.bimestre = bimestre
        self.data_aplicacao = data_aplicacao
    
    def __str__(self):
        return f'{self.av_id} - {self.serie} Serie, {self.bimestre} Bimestre, {self.data_aplicacao}'
    

def create(av: Avaliacao, materia):
    """Insere uma nova avaliação no banco de dados"""

    connection, cursor = connect_db()

    try:
        av_id = generate_av_id(av, materia, cursor)

        cursor.execute('INSERT INTO avaliacoes (id, serie, bimestre, data_aplicacao) VALUES (?, ?, ?, ?)',
                       (av_id, av.serie, av.bimestre, av.data_aplicacao))
        connection.commit()
    
    except sqlite3.IntegrityError:
        print('ID duplicado')
    else:
        materias_avaliacoes(materia, av_id, cursor, connection)
    
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
    avs_2: list[Avaliacao] = [] # Lista de Objetos(Avaliações) com os dados da tabela

    for av in avs_1:
        avs_2.append(Avaliacao(av[0], av[1], av[2], av[3]))

    connection.close()

    return avs_2


def get(av_id):
    """Recupera uma avaliação do banco de dados"""
    connection, cursor = connect_db()

    cursor.execute('SELECT * FROM avaliacoes WHERE id = ?', (str(av_id),))
    row = cursor.fetchall()[0]
    avaliacao = Avaliacao(row[0], row[1], row[2], row[3])

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

