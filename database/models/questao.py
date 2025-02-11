import sqlite3
from database.scripts.banco import connect_db
from random import randint

class Questao:
    """Modelo de dados da tabela banco_de_questoes"""

    def __init__(self, q_id=0, enunciado='', serie='', materia='', assunto='', resposta='') -> None:
        self.q_id = q_id
        self.enunciado = enunciado
        self.serie = serie
        self.materia = materia
        self.assunto = assunto
        self.resposta = resposta

    def __str__(self) -> str:
        return f"{self.q_id} {self.enunciado}"


def create(questao: Questao):
    """Insere uma nova questão no banco de dados"""
    connection, cursor = connect_db()

    try:
        questao_id = generate_question_id(questao, cursor)

        cursor.execute('INSERT INTO questoes (id, enunciado, serie, materia, assunto, resposta) VALUES (?, ?, ?, ?, ?, ?)',
                       (questao_id, questao.enunciado, questao.serie, questao.materia, questao.assunto, questao.resposta))
        connection.commit()


    except sqlite3.IntegrityError:
        print('ID duplicado')
    else:
        questao.q_id = questao_id

    connection.close()


def delete(questao_id):
    """Deleta uma questão do banco de dados"""
    connection, cursor = connect_db()

    cursor.execute('DELETE FROM questoes WHERE id = ?', (str(questao_id),))
    connection.commit()

    connection.close()


def list_questions(limit=None):
    """Retorna todas as questões cadastradas no banco de dados"""
    connection, cursor = connect_db()

    if limit == None:
        cursor.execute('SELECT * FROM questoes')
    elif limit != None:
        cursor.execute('SELECT * FROM questoes LIMIT ?', (str(limit),))

    questoes_1 = cursor.fetchall()  # Lista com os dados da tabela
    questoes_2: list[Questao] = []  # Lista de objetos Questao

    for questao in questoes_1:
        questoes_2.append(Questao(*questao))

    connection.close()

    return questoes_2


def get(questao_id):
    """Retorna uma questão específica do banco de dados"""
    connection, cursor = connect_db()

    cursor.execute('SELECT * FROM questoes WHERE id = ?', (str(questao_id),))
    row = cursor.fetchone()

    if row:
        questao = Questao(*row)
    else:
        questao = None

    connection.close()

    return questao


def update(questao_id, questao: Questao):
    """Atualiza uma questão no banco de dados"""
    connection, cursor = connect_db()

    cursor.execute('UPDATE questoes SET enunciado = ?, serie = ?, materia = ?, assunto = ?, resposta = ? WHERE id = ?',
                   (questao.enunciado, questao.serie, questao.materia, questao.assunto, questao.resposta, questao_id))
    
    connection.commit()
    connection.close()


def generate_question_id(questao: Questao, cursor):
    """Gera um ID único para a questão"""
    q_id = str(questao.serie)

    cursor.execute('SELECT id FROM materias WHERE nome = ?', (questao.materia,))
    id_materia = cursor.fetchall()[0][0]
    q_id += str(id_materia)

    for _ in range(6):
        q_id += str(randint(0, 9))
    return q_id


def list_questions_filtered(serie, materia, assunto):
    """Lista as questões de acordo com filtros"""
    query = 'SELECT * FROM questoes WHERE '
    params = []
    questions = []
    flag_serie = flag_materia = flag_assunto = False

    if serie != 'todas':
        query += 'serie = ?'
        flag_serie = True
        params.append(serie)
    if materia != 'todas':
        if flag_serie:
            query += ' AND '
        query += 'materia = ?'
        flag_materia = True
        params.append(materia)
    if assunto != '':
        if flag_serie or flag_materia:
            query += ' AND '
        query += 'assunto = ?'
        flag_assunto = True
        params.append(assunto)
    
    if len(params) != 0:
        connection, cursor = connect_db()
        cursor.execute(query, tuple(params))
        rows = cursor.fetchall()
        connection.close()

        print(query, params)

        for row in rows:
            questions.append(Questao(*row))
    else:
        questions = list_questions()
    
    return questions
        
