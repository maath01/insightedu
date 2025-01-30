import sqlite3
from database.banco import connect_db
import database.avaliacao as avl
import database.turma as turma
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

def update(nota_id, nota: Nota):
    """Atualiza um elemento no banco de dados"""
    connection, cursor = connect_db()

    cursor.execute('UPDATE notas SET aluno_id = ?, avaliacao_id = ?, nota = ? WHERE id = ?',
                (nota.al_id, nota.av_id, nota.nota, nota_id))
    
    connection.commit()
    connection.close()

def generate_nota_id(al_id, av_id):
    """Gera um ID único para a nota."""
    nota_id = f"{al_id}{str(av_id)[0:3]}"

    for _ in range(2):
        nota_id += str(randint(0, 9))
    
    return nota_id


def get_student_notes(al_id):
    """Devolve todas as notas de um aluno"""

    connection, cursor = connect_db()

    cursor.execute('SELECT * FROM notas WHERE aluno_id = ?', (str(al_id),))
    rows = cursor.fetchall()
    connection.close()

    notas = {
        '1 ano': {'Português': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Matêmatica': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Ciencias': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Geografia': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Historia': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}},
        '2 ano': {'Português': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Matêmatica': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Ciencias': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Geografia': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Historia': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}},
        '3 ano': {'Português': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Matêmatica': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Ciencias': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Geografia': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Historia': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}},
        '4 ano': {'Português': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Matêmatica': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Ciencias': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Geografia': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Historia': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}},
        '5 ano': {'Português': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Matêmatica': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Ciencias': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Geografia': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Historia': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}},
        '6 ano': {'Português': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Matêmatica': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Ciencias': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Geografia': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Historia': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}},
        '7 ano': {'Português': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Matêmatica': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Ciencias': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Geografia': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Historia': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}},
        '8 ano': {'Português': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Matêmatica': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Ciencias': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Geografia': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Historia': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}},
        '9 ano': {'Português': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Matêmatica': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Ciencias': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Geografia': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Historia': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}},
        }

    for row in rows:
        av = avl.get(row[2])
        materia = avl.get_matter(av)

        notas[f'{str(av.serie)} ano'][materia][f'{str(av.bimestre)} bim'] = row[3]

    return notas


def get_student_average_general(al_id, serie):
    """Calcula a media de um aluno em uma determinada serie"""

    notes = get_student_notes(al_id)
    soma = 0
    count = 0

    for materia in notes[f'{str(serie)} ano'].values():
        for nota in materia.values():
            if nota != None:
                soma += nota
                count += 1
    try:
        media = soma/count
    except ZeroDivisionError:
        return 0
    
    return media


def get_student_average_by_bim(al_id, serie, bimestre):
    """Calcula a media de um aluno em uma determinada serie e bimestre"""
    notes = get_student_notes(al_id)
    soma = 0
    count = 0

    for materia in notes[f'{str(serie)} ano'].values():
        for bim, nota in materia.items():
            if nota != None and bim[0] == str(bimestre):
                soma += nota
                count += 1
    
    try:
        media = soma/count
    except ZeroDivisionError:
        return 0
    return media


def get_class_average_general(alunos, tur_id):
    """Calcula a media de uma classe"""

    turma_ = turma.get(tur_id)
    soma = 0
    count = 0

    for aluno in alunos:
        media = get_student_average_general(aluno.al_id, turma_.serie)
        soma += media
        count += 1
    
    try:
        media = soma/count
    except ZeroDivisionError:
        return 0

    return media


def get_class_average_by_bim_and_matter(alunos, turma_id, bimestre, materia):
    """Devolve a media da classe em uma materia em um determinado bimestre"""
    turma_ = turma.get(turma_id)
    soma = 0
    count = 0

    for aluno in alunos:
        notes = get_student_notes(aluno.al_id)
        nota = acess_notes_data(notes, turma_.serie, bimestre, materia)
        if nota != None:
            soma += nota
            count += 1
    
    try:
        media = soma/count
    except ZeroDivisionError:
        return 0

    return media


def acess_notes_data(notes: dict, serie: int, bimestre: int, materia: str):
    """Recebe um dicionario de notas, juntamente a serie, o bimestre e a materia e devolve a nota correspondente"""
    if 0 <= serie >= 10:
        return None
    if 0 <= bimestre >= 5:
        return None
    
    nota = notes[f'{str(serie)} ano'][materia][f'{str(bimestre)} bim']
    return nota
